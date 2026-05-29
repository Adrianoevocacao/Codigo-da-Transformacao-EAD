"""
Atividade 3 — Flask conectado ao SQLite para persistir usuários.
Para instalar: pip install flask
Para rodar:    python app.py

Rotas disponíveis:
  GET  /saudacao         → mensagem de boas-vindas
  POST /cadastrar        → cadastra usuário (nome, email)
  GET  /usuarios         → lista todos os usuários
  GET  /usuarios/<id>    → busca usuário por ID
  DELETE /usuarios/<id>  → deleta usuário por ID
"""

import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)
BANCO = "usuarios.db"


# =============================================
#   BANCO DE DADOS
# =============================================

def init_db():
    """Cria o banco e a tabela se não existirem."""
    with sqlite3.connect(BANCO) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS Usuarios (
                id    INTEGER PRIMARY KEY AUTOINCREMENT,
                nome  TEXT    NOT NULL,
                email TEXT    NOT NULL UNIQUE
            )
        """)
    print("✅ Banco de dados 'usuarios.db' pronto!")


def get_db():
    conn = sqlite3.connect(BANCO)
    conn.row_factory = sqlite3.Row
    return conn


# =============================================
#   ROTAS
# =============================================

@app.route("/saudacao", methods=["GET"])
def saudacao():
    return jsonify({
        "mensagem": "Olá! API Flask + SQLite funcionando! 🚀",
        "status":   "online"
    }), 200


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Nenhum dado enviado."}), 400
    if "nome" not in dados or "email" not in dados:
        return jsonify({"erro": "Campos 'nome' e 'email' são obrigatórios."}), 400

    try:
        with get_db() as conn:
            cursor = conn.execute(
                "INSERT INTO Usuarios (nome, email) VALUES (?, ?)",
                (dados["nome"], dados["email"])
            )
            novo_id = cursor.lastrowid

        return jsonify({
            "mensagem": "Usuário cadastrado com sucesso!",
            "usuario": {"id": novo_id, "nome": dados["nome"], "email": dados["email"]}
        }), 201

    except sqlite3.IntegrityError:
        return jsonify({"erro": "Email já cadastrado."}), 409


@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    with get_db() as conn:
        usuarios = conn.execute("SELECT * FROM Usuarios ORDER BY nome").fetchall()
    return jsonify([dict(u) for u in usuarios]), 200


@app.route("/usuarios/<int:id>", methods=["GET"])
def buscar_usuario(id):
    with get_db() as conn:
        usuario = conn.execute(
            "SELECT * FROM Usuarios WHERE id = ?", (id,)
        ).fetchone()
    if usuario:
        return jsonify(dict(usuario)), 200
    return jsonify({"erro": "Usuário não encontrado."}), 404


@app.route("/usuarios/<int:id>", methods=["DELETE"])
def deletar_usuario(id):
    with get_db() as conn:
        cursor = conn.execute("DELETE FROM Usuarios WHERE id = ?", (id,))
    if cursor.rowcount:
        return jsonify({"mensagem": f"Usuário ID {id} deletado!"}), 200
    return jsonify({"erro": "Usuário não encontrado."}), 404


# =============================================
#   INICIALIZAÇÃO
# =============================================

if __name__ == "__main__":
    init_db()
    print("✅ Servidor rodando em http://localhost:5000")
    app.run(debug=True)
