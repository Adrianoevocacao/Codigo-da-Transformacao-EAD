"""
Atividade 2 — Views para cadastro, listagem, atualização e exclusão de produtos.
Arquivo: views.py — coloque em produtos/views.py
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Produto
from .forms import ProdutoForm


def listar_produtos(request):
    """Lista todos os produtos."""
    produtos = Produto.objects.all()
    return render(request, "produtos/lista.html", {"produtos": produtos})


def detalhar_produto(request, pk):
    """Exibe detalhes de um produto."""
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, "produtos/detalhe.html", {"produto": produto})


def cadastrar_produto(request):
    """Cadastra um novo produto."""
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Produto cadastrado com sucesso!")
            return redirect("listar_produtos")
    else:
        form = ProdutoForm()
    return render(request, "produtos/formulario.html", {"form": form, "titulo": "Cadastrar Produto"})


def atualizar_produto(request, pk):
    """Atualiza um produto existente."""
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Produto atualizado com sucesso!")
            return redirect("listar_produtos")
    else:
        form = ProdutoForm(instance=produto)
    return render(request, "produtos/formulario.html", {"form": form, "titulo": "Atualizar Produto"})


def excluir_produto(request, pk):
    """Exclui um produto."""
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        produto.delete()
        messages.success(request, "🗑️ Produto excluído com sucesso!")
        return redirect("listar_produtos")
    return render(request, "produtos/confirmar_exclusao.html", {"produto": produto})
