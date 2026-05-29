"""
Atividade 3 — Testes automatizados para o app produtos.
Arquivo: tests.py — coloque em produtos/tests.py
Para rodar: python manage.py test produtos
"""

from django.test import TestCase, Client
from django.urls import reverse
from .models import Produto


class ProdutoModelTest(TestCase):
    """Testa o modelo Produto."""

    def setUp(self):
        self.produto = Produto.objects.create(
            nome="Notebook",
            descricao="Notebook gamer",
            preco=3500.00,
            quantidade=10
        )

    def test_produto_criado_corretamente(self):
        """Produto deve ser criado com os dados corretos."""
        self.assertEqual(self.produto.nome, "Notebook")
        self.assertEqual(float(self.produto.preco), 3500.00)
        self.assertEqual(self.produto.quantidade, 10)

    def test_str_produto(self):
        """__str__ deve retornar nome e preço."""
        self.assertIn("Notebook", str(self.produto))

    def test_em_estoque_verdadeiro(self):
        """Produto com quantidade > 0 deve estar em estoque."""
        self.assertTrue(self.produto.em_estoque())

    def test_em_estoque_falso(self):
        """Produto com quantidade 0 não deve estar em estoque."""
        self.produto.quantidade = 0
        self.produto.save()
        self.assertFalse(self.produto.em_estoque())


class ProdutoViewTest(TestCase):
    """Testa as views do app produtos."""

    def setUp(self):
        self.client = Client()
        self.produto = Produto.objects.create(
            nome="Mouse",
            descricao="Mouse sem fio",
            preco=150.00,
            quantidade=5
        )

    def test_listar_produtos_retorna_200(self):
        """GET / deve retornar status 200."""
        response = self.client.get(reverse("listar_produtos"))
        self.assertEqual(response.status_code, 200)

    def test_listar_exibe_produto(self):
        """Lista deve conter o produto cadastrado."""
        response = self.client.get(reverse("listar_produtos"))
        self.assertContains(response, "Mouse")

    def test_cadastrar_produto_post(self):
        """POST válido deve criar produto e redirecionar."""
        response = self.client.post(reverse("cadastrar_produto"), {
            "nome":       "Teclado",
            "descricao":  "Teclado mecânico",
            "preco":      "250.00",
            "quantidade": "3"
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Produto.objects.filter(nome="Teclado").exists())

    def test_excluir_produto(self):
        """POST para excluir deve remover o produto."""
        response = self.client.post(reverse("excluir_produto", args=[self.produto.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Produto.objects.filter(pk=self.produto.pk).exists())
