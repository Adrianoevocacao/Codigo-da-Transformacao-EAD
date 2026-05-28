"""
Desafio Extra — Gerenciador de Tarefas com SQLite.
Adiciona, visualiza, conclui e exclui tarefas.
Não precisa instalar nada — sqlite3 já vem com Python!
"""

import sqlite3
from datetime import datetime


def criar_tabela():
    conn = sqlite3.connect("tarefas.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS Tarefas (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo    TEXT    NOT NULL,
            concluida INTEGER NOT NULL DEFAULT 0,
            criada_em TEXT    NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def adicionar_tarefa(titulo):
    conn = sqlite3.connect("tarefas.db")
    conn.execute(
        "INSERT INTO Tarefas (titulo, criada_em) VALUES (?, ?)",
        (titulo, datetime.now().strftime("%d/%m/%Y %H:%M"))
    )
    conn.commit()
    conn.close()
    print(f"✅ Tarefa '{titulo}' adicionada!")


def visualizar_tarefas():
    conn = sqlite3.connect("tarefas.db")
    tarefas = conn.execute("SELECT * FROM Tarefas ORDER BY id").fetchall()
    conn.close()

    print("\n📋 LISTA DE TAREFAS:")
    print("=" * 50)
    if not tarefas:
        print("  Nenhuma tarefa cadastrada.")
    for t in tarefas:
        status = "✅" if t[3] else "⏳"
        print(f"  [{t[0]}] {status} {t[1]}  ({t[2]})")
    print("=" * 50)


def concluir_tarefa(id_tarefa):
    conn = sqlite3.connect("tarefas.db")
    cursor = conn.execute(
        "UPDATE Tarefas SET concluida = 1 WHERE id = ? AND concluida = 0",
        (id_tarefa,)
    )
    conn.commit()
    conn.close()
    if cursor.rowcount:
        print(f"🎉 Tarefa ID {id_tarefa} concluída!")
    else:
        print(f"⚠️  Tarefa ID {id_tarefa} não encontrada ou já concluída.")


def excluir_tarefa(id_tarefa):
    conn = sqlite3.connect("tarefas.db")
    cursor = conn.execute("DELETE FROM Tarefas WHERE id = ?", (id_tarefa,))
    conn.commit()
    conn.close()
    if cursor.rowcount:
        print(f"🗑️  Tarefa ID {id_tarefa} excluída!")
    else:
        print(f"❌ Tarefa ID {id_tarefa} não encontrada.")


def menu():
    print("\n" + "=" * 45)
    print("     ✅ GERENCIADOR DE TAREFAS")
    print("=" * 45)
    print("  1. Adicionar tarefa")
    print("  2. Visualizar tarefas")
    print("  3. Concluir tarefa")
    print("  4. Excluir tarefa")
    print("  0. Sair")
    print("=" * 45)
    return input("Opção: ").strip()


if __name__ == "__main__":
    criar_tabela()

    while True:
        opcao = menu()

        if opcao == "1":
            titulo = input("Título da tarefa: ").strip()
            if titulo:
                adicionar_tarefa(titulo)
            else:
                print("⚠️  O título é obrigatório.")

        elif opcao == "2":
            visualizar_tarefas()

        elif opcao == "3":
            visualizar_tarefas()
            try:
                id_t = int(input("ID da tarefa a concluir: "))
                concluir_tarefa(id_t)
            except ValueError:
                print("⚠️  Digite um ID válido.")

        elif opcao == "4":
            visualizar_tarefas()
            try:
                id_t = int(input("ID da tarefa a excluir: "))
                excluir_tarefa(id_t)
            except ValueError:
                print("⚠️  Digite um ID válido.")

        elif opcao == "0":
            print("👋 Encerrando.")
            break
        else:
            print("⚠️  Opção inválida.")
