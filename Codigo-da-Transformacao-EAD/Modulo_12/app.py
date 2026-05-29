"""
Desafio Extra — API Flask simples para ser testada.
Para instalar: pip install flask
Para rodar a API: python app.py
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Banco de dados em memória
tarefas = [
    {"id": 1, "titulo": "Estudar Python", "concluida": False},
    {"id": 2, "titulo": "Fazer commits",  "concluida": True},
]


@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas), 200


@app.route("/tarefas/<int:id>", methods=["GET"])
def buscar_tarefa(id):
    tarefa = next((t for t in tarefas if t["id"] == id), None)
    if tarefa:
        return jsonify(tarefa), 200
    return jsonify({"erro": "Tarefa não encontrada"}), 404


@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    dados = request.get_json()
    if not dados or "titulo" not in dados:
        return jsonify({"erro": "Campo 'titulo' é obrigatório"}), 400
    nova = {
        "id":       len(tarefas) + 1,
        "titulo":   dados["titulo"],
        "concluida": False,
    }
    tarefas.append(nova)
    return jsonify(nova), 201


@app.route("/tarefas/<int:id>", methods=["DELETE"])
def deletar_tarefa(id):
    tarefa = next((t for t in tarefas if t["id"] == id), None)
    if not tarefa:
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    tarefas.remove(tarefa)
    return jsonify({"mensagem": "Tarefa deletada"}), 200


if __name__ == "__main__":
    app.run(debug=True)
