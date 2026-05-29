"""
Atividade 2 — Rota POST /cadastrar para receber dados via JSON.
Para instalar: pip install flask
Para rodar:    python app.py

Teste com curl:
curl -X POST http://localhost:5000/cadastrar \
     -H "Content-Type: application/json" \
     -d '{"nome": "Ana Silva", "email": "ana@gmail.com"}'
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista em memória para guardar os usuários
usuarios = []


@app.route("/saudacao", methods=["GET"])
def saudacao():
    return jsonify({"mensagem": "Olá! Bem-vindo à API! 🚀"}), 200


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.get_json()

    # Valida se os campos obrigatórios foram enviados
    if not dados:
        return jsonify({"erro": "Nenhum dado enviado."}), 400
    if "nome" not in dados or "email" not in dados:
        return jsonify({"erro": "Campos 'nome' e 'email' são obrigatórios."}), 400

    # Verifica se email já existe
    for u in usuarios:
        if u["email"] == dados["email"]:
            return jsonify({"erro": "Email já cadastrado."}), 409

    usuario = {
        "id":    len(usuarios) + 1,
        "nome":  dados["nome"],
        "email": dados["email"]
    }
    usuarios.append(usuario)

    return jsonify({
        "mensagem": "Usuário cadastrado com sucesso!",
        "usuario":  usuario
    }), 201


@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios), 200


if __name__ == "__main__":
    print("✅ Servidor rodando em http://localhost:5000")
    app.run(debug=True)
