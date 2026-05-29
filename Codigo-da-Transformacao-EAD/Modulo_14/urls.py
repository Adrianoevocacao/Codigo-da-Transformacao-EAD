"""
Atividade 2 — Rotas do app produtos.
Arquivo: urls.py — coloque em produtos/urls.py
e inclua no urls.py principal com: path('', include('produtos.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path("",                      views.listar_produtos,   name="listar_produtos"),
    path("novo/",                 views.cadastrar_produto, name="cadastrar_produto"),
    path("<int:pk>/",             views.detalhar_produto,  name="detalhar_produto"),
    path("<int:pk>/editar/",      views.atualizar_produto, name="atualizar_produto"),
    path("<int:pk>/excluir/",     views.excluir_produto,   name="excluir_produto"),
]
