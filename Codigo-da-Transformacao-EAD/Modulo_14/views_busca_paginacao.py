"""
Desafio Extra — Busca por nome e paginação na listagem de produtos.
Substitui o views.py da atividade 2 com essas melhorias.
Arquivo: views_busca_paginacao.py — coloque em produtos/views.py
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Produto
from .forms import ProdutoForm


def listar_produtos(request):
    """Lista produtos com busca por nome e paginação."""
    busca = request.GET.get("busca", "").strip()

    produtos = Produto.objects.all()
    if busca:
        produtos = produtos.filter(nome__icontains=busca)

    # Paginação: 5 produtos por página
    paginador = Paginator(produtos, 5)
    pagina    = request.GET.get("pagina", 1)
    produtos_paginados = paginador.get_page(pagina)

    return render(request, "produtos/lista.html", {
        "produtos": produtos_paginados,
        "busca":    busca,
        "total":    produtos.count(),
    })


def detalhar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, "produtos/detalhe.html", {"produto": produto})


def cadastrar_produto(request):
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
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Produto atualizado!")
            return redirect("listar_produtos")
    else:
        form = ProdutoForm(instance=produto)
    return render(request, "produtos/formulario.html", {"form": form, "titulo": "Atualizar Produto"})


def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        produto.delete()
        messages.success(request, "🗑️ Produto excluído!")
        return redirect("listar_produtos")
    return render(request, "produtos/confirmar_exclusao.html", {"produto": produto})
