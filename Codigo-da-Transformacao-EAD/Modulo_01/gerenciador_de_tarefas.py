"""
Gerenciador de Tarefas - CLI
Projeto simples para adicionar, listar, concluir e remover tarefas.
"""

import json
import os
from datetime import datetime

ARQUIVO = "tarefas.json"


def carregar_tarefas():
    """Carrega as tarefas do arquivo JSON."""
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_tarefas(tarefas):
    """Salva as tarefas no arquivo JSON."""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=2)


def adicionar_tarefa(descricao):
    """Adiciona uma nova tarefa."""
    tarefas = carregar_tarefas()
    tarefa = {
        "id": len(tarefas) + 1,
        "descricao": descricao,
        "concluida": False,
        "criada_em": datetime.now().strftime("%d/%m/%Y %H:%M")
    }
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print(f"✅ Tarefa '{descricao}' adicionada com sucesso!")


def listar_tarefas():
    """Lista todas as tarefas."""
    tarefas = carregar_tarefas()
    if not tarefas:
        print("📭 Nenhuma tarefa encontrada.")
        return
    print("\n📋 Lista de Tarefas:")
    print("-" * 40)
    for t in tarefas:
        status = "✔️ " if t["concluida"] else "⏳"
        print(f"[{t['id']}] {status} {t['descricao']}  ({t['criada_em']})")
    print("-" * 40)


def concluir_tarefa(id_tarefa):
    """Marca uma tarefa como concluída."""
    tarefas = carregar_tarefas()
    for t in tarefas:
        if t["id"] == id_tarefa:
            t["concluida"] = True
            salvar_tarefas(tarefas)
            print(f"🎉 Tarefa '{t['descricao']}' marcada como concluída!")
            return
    print(f"❌ Tarefa com ID {id_tarefa} não encontrada.")


def remover_tarefa(id_tarefa):
    """Remove uma tarefa pelo ID."""
    tarefas = carregar_tarefas()
    nova_lista = [t for t in tarefas if t["id"] != id_tarefa]
    if len(nova_lista) == len(tarefas):
        print(f"❌ Tarefa com ID {id_tarefa} não encontrada.")
        return
    salvar_tarefas(nova_lista)
    print(f"🗑️  Tarefa removida com sucesso!")


def menu():
    """Exibe o menu principal."""
    print("\n============================")
    print("   GERENCIADOR DE TAREFAS   ")
    print("============================")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("0. Sair")
    print("============================")
    return input("Escolha uma opção: ").strip()


def main():
    while True:
        opcao = menu()
        if opcao == "1":
            descricao = input("Descrição da tarefa: ").strip()
            if descricao:
                adicionar_tarefa(descricao)
            else:
                print("⚠️  A descrição não pode ser vazia.")
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            listar_tarefas()
            try:
                id_t = int(input("ID da tarefa a concluir: "))
                concluir_tarefa(id_t)
            except ValueError:
                print("⚠️  Digite um número válido.")
        elif opcao == "4":
            listar_tarefas()
            try:
                id_t = int(input("ID da tarefa a remover: "))
                remover_tarefa(id_t)
            except ValueError:
                print("⚠️  Digite um número válido.")
        elif opcao == "0":
            print("👋 Até mais!")
            break
        else:
            print("⚠️  Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()