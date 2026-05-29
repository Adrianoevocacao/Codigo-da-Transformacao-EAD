"""
Desafio Extra — Testes automatizados para a API Flask usando pytest.
Para instalar: pip install flask pytest
Para rodar:    pytest test_app.py -v
"""

import pytest
from app import app, tarefas


@pytest.fixture
def cliente():
    """Cria um cliente de teste do Flask antes de cada teste."""
    app.config["TESTING"] = True
    with app.test_client() as cliente:
        yield cliente


@pytest.fixture(autouse=True)
def resetar_tarefas():
    """Reseta a lista de tarefas antes de cada teste."""
    tarefas.clear()
    tarefas.extend([
        {"id": 1, "titulo": "Estudar Python", "concluida": False},
        {"id": 2, "titulo": "Fazer commits",  "concluida": True},
    ])


# =============================================
#   TESTES — GET /tarefas
# =============================================

def test_listar_tarefas_retorna_200(cliente):
    """GET /tarefas deve retornar status 200."""
    resposta = cliente.get("/tarefas")
    assert resposta.status_code == 200


def test_listar_tarefas_retorna_lista(cliente):
    """GET /tarefas deve retornar uma lista com 2 tarefas."""
    resposta = cliente.get("/tarefas")
    dados = resposta.get_json()
    assert isinstance(dados, list)
    assert len(dados) == 2


# =============================================
#   TESTES — GET /tarefas/<id>
# =============================================

def test_buscar_tarefa_existente(cliente):
    """GET /tarefas/1 deve retornar a tarefa correta."""
    resposta = cliente.get("/tarefas/1")
    assert resposta.status_code == 200
    dados = resposta.get_json()
    assert dados["titulo"] == "Estudar Python"


def test_buscar_tarefa_inexistente(cliente):
    """GET /tarefas/999 deve retornar status 404."""
    resposta = cliente.get("/tarefas/999")
    assert resposta.status_code == 404


# =============================================
#   TESTES — POST /tarefas
# =============================================

def test_criar_tarefa_com_sucesso(cliente):
    """POST /tarefas com título válido deve retornar 201."""
    resposta = cliente.post(
        "/tarefas",
        json={"titulo": "Nova tarefa"}
    )
    assert resposta.status_code == 201
    dados = resposta.get_json()
    assert dados["titulo"] == "Nova tarefa"
    assert dados["concluida"] is False


def test_criar_tarefa_sem_titulo(cliente):
    """POST /tarefas sem título deve retornar 400."""
    resposta = cliente.post("/tarefas", json={})
    assert resposta.status_code == 400


def test_criar_tarefa_sem_body(cliente):
    """POST /tarefas sem body deve retornar 400."""
    resposta = cliente.post("/tarefas")
    assert resposta.status_code == 400


# =============================================
#   TESTES — DELETE /tarefas/<id>
# =============================================

def test_deletar_tarefa_existente(cliente):
    """DELETE /tarefas/1 deve retornar 200."""
    resposta = cliente.delete("/tarefas/1")
    assert resposta.status_code == 200


def test_deletar_tarefa_inexistente(cliente):
    """DELETE /tarefas/999 deve retornar 404."""
    resposta = cliente.delete("/tarefas/999")
    assert resposta.status_code == 404
