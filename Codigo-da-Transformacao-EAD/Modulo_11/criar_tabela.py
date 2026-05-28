"""
Atividade 1 — Crie uma tabela Clientes com colunas id, nome, email.
Configura o banco de dados SQLite e cria a tabela.
"""

import sqlite3

def criar_tabela():
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Clientes (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            nome  TEXT    NOT NULL,
            email TEXT    NOT NULL UNIQUE
        )
    """)

    conn.commit()
    conn.close()
    print("✅ Banco de dados 'clientes.db' criado!")
    print("✅ Tabela 'Clientes' criada com colunas: id, nome, email")

if __name__ == "__main__":
    criar_tabela()
