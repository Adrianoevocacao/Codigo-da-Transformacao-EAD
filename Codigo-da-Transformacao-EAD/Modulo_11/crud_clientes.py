"""
Atividade 2 — CRUD: Inserir, consultar, atualizar e deletar registros.
Execute criar_tabela.py antes de rodar este arquivo!
"""

import sqlite3

def inserir_cliente(nome, email):
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO Clientes (nome, email) VALUES (?, ?)",
            (nome, email)
        )
        conn.commit()
        print(f"✅ Cliente '{nome}' inserido com sucesso!")
    except sqlite3.IntegrityError:
        print(f"❌ Email '{email}' já cadastrado.")
    finally:
        conn.close()


def consultar_clientes():
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Clientes ORDER BY nome")
    clientes = cursor.fetchall()
    conn.close()

    print("\n📋 TODOS OS CLIENTES:")
    print("=" * 45)
    if not clientes:
        print("  Nenhum cliente cadastrado.")
    for c in clientes:
        print(f"  ID: {c[0]} | Nome: {c[1]} | Email: {c[2]}")
    print("=" * 45)


def atualizar_cliente(id_cliente, novo_nome, novo_email):
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Clientes SET nome = ?, email = ? WHERE id = ?",
        (novo_nome, novo_email, id_cliente)
    )
    conn.commit()
    conn.close()

    if cursor.rowcount:
        print(f"✅ Cliente ID {id_cliente} atualizado!")
    else:
        print(f"❌ Cliente ID {id_cliente} não encontrado.")


def deletar_cliente(id_cliente):
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Clientes WHERE id = ?", (id_cliente,))
    conn.commit()
    conn.close()

    if cursor.rowcount:
        print(f"🗑️  Cliente ID {id_cliente} deletado!")
    else:
        print(f"❌ Cliente ID {id_cliente} não encontrado.")


if __name__ == "__main__":
    print("=" * 45)
    print("   CRUD — TABELA CLIENTES")
    print("=" * 45)

    # INSERT
    print("\n➕ Inserindo clientes...")
    inserir_cliente("Ana Silva",   "ana@gmail.com")
    inserir_cliente("Bruno Costa", "bruno@hotmail.com")
    inserir_cliente("Carla Souza", "carla@gmail.com")
    inserir_cliente("Diego Lima",  "diego@yahoo.com")

    # SELECT
    consultar_clientes()

    # UPDATE
    print("\n✏️  Atualizando cliente ID 1...")
    atualizar_cliente(1, "Ana Paula Silva", "anapaula@gmail.com")
    consultar_clientes()

    # DELETE
    print("\n🗑️  Deletando cliente ID 4...")
    deletar_cliente(4)
    consultar_clientes()
