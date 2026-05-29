"""
Atividade 2 — Formulário do Produto.
Arquivo: forms.py — coloque em produtos/forms.py
"""

from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "descricao", "preco", "quantidade"]
        widgets = {
            "nome":       forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome do produto"}),
            "descricao":  forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Descrição"}),
            "preco":      forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "quantidade": forms.NumberInput(attrs={"class": "form-control", "min": "0"}),
        }
        labels = {
            "nome":       "Nome",
            "descricao":  "Descrição",
            "preco":      "Preço (R$)",
            "quantidade": "Quantidade em estoque",
        }
