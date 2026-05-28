"""
Atividade 3 — Consultas SQL para filtrar dados.
Execute criar_tabela.py e crud_clientes.py antes deste arquivo!
"""

import sqlite3

def buscar_por_letra(letra):
    """Busca clientes cujo nome começa com determinada letra."""
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM Clientes WHERE nome LIKE ? ORDER BY nome",
        (f"{letra}%",)
    )
    clientes = cursor.fetchall()
    conn.close()

    print(f"\n🔍 Clientes com nome começando em '{letra.upper()}':")
    print("-" * 45)
    if not clientes:
        print("  Nenhum resultado encontrado.")
    for c in clientes:
        print(f"  ID: {c[0]} | Nome: {c[1]} | Email: {c[2]}")
    print("-" * 45)


def buscar_por_dominio(dominio):
    """Busca clientes com determinado domínio de email."""
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM Clientes WHERE email LIKE ? ORDER BY nome",
        (f"%@{dominio}",)
    )
    clientes = cursor.fetchall()
    conn.close()

    print(f"\n🔍 Clientes com email '@{dominio}':")
    print("-" * 45)
    if not clientes:
        print("  Nenhum resultado encontrado.")
    for c in clientes:
        print(f"  ID: {c[0]} | Nome: {c[1]} | Email: {c[2]}")
    print("-" * 45)


def contar_clientes():
    """Conta o total de clientes cadastrados."""
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Clientes")
    total = cursor.fetchone()[0]
    conn.close()
    print(f"\n📊 Total de clientes cadastrados: {total}")


if __name__ == "__main__":
    print("=" * 45)
    print("   CONSULTAS SQL FILTRADAS")
    print("=" * 45)

    buscar_por_letra("A")
    buscar_por_letra("C")
    buscar_por_dominio("gmail.com")
    buscar_por_dominio("hotmail.com")
    contar_clientes()
