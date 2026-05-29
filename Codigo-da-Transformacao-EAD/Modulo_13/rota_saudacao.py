"""
Atividade 1 — Servidor Flask com rota GET /saudacao.
Para instalar: pip install flask
Para rodar:    python app.py
Acesse:        http://localhost:5000/saudacao
"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/saudacao", methods=["GET"])
def saudacao():
    return jsonify({
        "mensagem": "Olá! Bem-vindo à minha API Flask! 🚀",
        "status":   "online"
    }), 200


if __name__ == "__main__":
    print("✅ Servidor rodando em http://localhost:5000")
    app.run(debug=True)
