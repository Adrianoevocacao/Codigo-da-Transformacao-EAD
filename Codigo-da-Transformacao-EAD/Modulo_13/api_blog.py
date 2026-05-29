"""
Desafio Extra — API completa para Blog.
Funcionalidades: posts, comentários e autenticação de usuários.
Para instalar: pip install flask
Para rodar:    python app.py

ROTAS:
  AUTH
    POST /registrar          → registra usuário
    POST /login              → faz login e retorna token simples

  POSTS
    GET  /posts              → lista todos os posts
    GET  /posts/<id>         → busca post por ID
    POST /posts              → cria post (requer token)
    DELETE /posts/<id>       → deleta post (requer token)

  COMENTÁRIOS
    GET  /posts/<id>/comentarios       → lista comentários do post
    POST /posts/<id>/comentarios       → adiciona comentário (requer token)
"""

import sqlite3
import hashlib
from flask import Flask, jsonify, request

app = Flask(__name__)
BANCO = "blog.db"


# =============================================
#   BANCO DE DADOS
# =============================================

def init_db():
    with sqlite3.connect(BANCO) as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS Usuarios (
                id    INTEGER PRIMARY KEY AUTOINCREMENT,
                nome  TEXT    NOT NULL,
                email TEXT    NOT NULL UNIQUE,
                senha TEXT    NOT NULL
            );
            CREATE TABLE IF NOT EXISTS Posts (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo     TEXT NOT NULL,
                conteudo   TEXT NOT NULL,
                autor_id   INTEGER NOT NULL,
                criado_em  TEXT NOT NULL DEFAULT (datetime('now','localtime')),
                FOREIGN KEY (autor_id) REFERENCES Usuarios(id)
            );
            CREATE TABLE IF NOT EXISTS Comentarios (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                post_id   INTEGER NOT NULL,
                autor_id  INTEGER NOT NULL,
                texto     TEXT    NOT NULL,
                criado_em TEXT    NOT NULL DEFAULT (datetime('now','localtime')),
                FOREIGN KEY (post_id)  REFERENCES Posts(id),
                FOREIGN KEY (autor_id) REFERENCES Usuarios(id)
            );
        """)
    print("✅ Banco 'blog.db' pronto!")


def get_db():
    conn = sqlite3.connect(BANCO)
    conn.row_factory = sqlite3.Row
    return conn


def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()


def verificar_token(req):
    """Token simples: 'Bearer email:senha_hash'"""
    auth = req.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return None
    token = auth.replace("Bearer ", "")
    with get_db() as conn:
        usuario = conn.execute(
            "SELECT * FROM Usuarios WHERE email || ':' || senha = ?", (token,)
        ).fetchone()
    return dict(usuario) if usuario else None


# =============================================
#   AUTH
# =============================================

@app.route("/registrar", methods=["POST"])
def registrar():
    dados = request.get_json()
    if not dados or not all(k in dados for k in ["nome", "email", "senha"]):
        return jsonify({"erro": "Campos 'nome', 'email' e 'senha' são obrigatórios."}), 400
    try:
        with get_db() as conn:
            conn.execute(
                "INSERT INTO Usuarios (nome, email, senha) VALUES (?, ?, ?)",
                (dados["nome"], dados["email"], hash_senha(dados["senha"]))
            )
        return jsonify({"mensagem": "Usuário registrado com sucesso!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"erro": "Email já cadastrado."}), 409


@app.route("/login", methods=["POST"])
def login():
    dados = request.get_json()
    if not dados or not all(k in dados for k in ["email", "senha"]):
        return jsonify({"erro": "Campos 'email' e 'senha' são obrigatórios."}), 400
    with get_db() as conn:
        usuario = conn.execute(
            "SELECT * FROM Usuarios WHERE email = ? AND senha = ?",
            (dados["email"], hash_senha(dados["senha"]))
        ).fetchone()
    if not usuario:
        return jsonify({"erro": "Email ou senha incorretos."}), 401
    token = f"{usuario['email']}:{usuario['senha']}"
    return jsonify({"mensagem": "Login realizado!", "token": f"Bearer {token}"}), 200


# =============================================
#   POSTS
# =============================================

@app.route("/posts", methods=["GET"])
def listar_posts():
    with get_db() as conn:
        posts = conn.execute("""
            SELECT p.id, p.titulo, p.conteudo, p.criado_em, u.nome AS autor
            FROM Posts p JOIN Usuarios u ON p.autor_id = u.id
            ORDER BY p.id DESC
        """).fetchall()
    return jsonify([dict(p) for p in posts]), 200


@app.route("/posts/<int:id>", methods=["GET"])
def buscar_post(id):
    with get_db() as conn:
        post = conn.execute("""
            SELECT p.id, p.titulo, p.conteudo, p.criado_em, u.nome AS autor
            FROM Posts p JOIN Usuarios u ON p.autor_id = u.id
            WHERE p.id = ?
        """, (id,)).fetchone()
    if not post:
        return jsonify({"erro": "Post não encontrado."}), 404
    return jsonify(dict(post)), 200


@app.route("/posts", methods=["POST"])
def criar_post():
    usuario = verificar_token(request)
    if not usuario:
        return jsonify({"erro": "Não autorizado. Faça login primeiro."}), 401
    dados = request.get_json()
    if not dados or not all(k in dados for k in ["titulo", "conteudo"]):
        return jsonify({"erro": "Campos 'titulo' e 'conteudo' são obrigatórios."}), 400
    with get_db() as conn:
        cursor = conn.execute(
            "INSERT INTO Posts (titulo, conteudo, autor_id) VALUES (?, ?, ?)",
            (dados["titulo"], dados["conteudo"], usuario["id"])
        )
    return jsonify({"mensagem": "Post criado!", "id": cursor.lastrowid}), 201


@app.route("/posts/<int:id>", methods=["DELETE"])
def deletar_post(id):
    usuario = verificar_token(request)
    if not usuario:
        return jsonify({"erro": "Não autorizado."}), 401
    with get_db() as conn:
        cursor = conn.execute("DELETE FROM Posts WHERE id = ?", (id,))
    if cursor.rowcount:
        return jsonify({"mensagem": "Post deletado!"}), 200
    return jsonify({"erro": "Post não encontrado."}), 404


# =============================================
#   COMENTÁRIOS
# =============================================

@app.route("/posts/<int:post_id>/comentarios", methods=["GET"])
def listar_comentarios(post_id):
    with get_db() as conn:
        comentarios = conn.execute("""
            SELECT c.id, c.texto, c.criado_em, u.nome AS autor
            FROM Comentarios c JOIN Usuarios u ON c.autor_id = u.id
            WHERE c.post_id = ?
            ORDER BY c.id ASC
        """, (post_id,)).fetchall()
    return jsonify([dict(c) for c in comentarios]), 200


@app.route("/posts/<int:post_id>/comentarios", methods=["POST"])
def adicionar_comentario(post_id):
    usuario = verificar_token(request)
    if not usuario:
        return jsonify({"erro": "Não autorizado."}), 401
    dados = request.get_json()
    if not dados or "texto" not in dados:
        return jsonify({"erro": "Campo 'texto' é obrigatório."}), 400
    with get_db() as conn:
        cursor = conn.execute(
            "INSERT INTO Comentarios (post_id, autor_id, texto) VALUES (?, ?, ?)",
            (post_id, usuario["id"], dados["texto"])
        )
    return jsonify({"mensagem": "Comentário adicionado!", "id": cursor.lastrowid}), 201


# =============================================
#   INICIALIZAÇÃO
# =============================================

if __name__ == "__main__":
    init_db()
    print("✅ Servidor rodando em http://localhost:5000")
    app.run(debug=True)
