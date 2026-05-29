"""
Atividade 3 — Painel de Administração Django.
Arquivo: admin.py — coloque em produtos/admin.py
"""

from django.contrib import admin
from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display   = ["id", "nome", "preco", "quantidade", "em_estoque", "criado_em"]
    list_filter    = ["criado_em"]
    search_fields  = ["nome", "descricao"]
    ordering       = ["nome"]
    list_per_page  = 20
    readonly_fields = ["criado_em", "atualizado_em"]

    fieldsets = (
        ("Informações do Produto", {
            "fields": ("nome", "descricao", "preco", "quantidade")
        }),
        ("Datas", {
            "fields": ("criado_em", "atualizado_em"),
            "classes": ("collapse",)
        }),
    )
