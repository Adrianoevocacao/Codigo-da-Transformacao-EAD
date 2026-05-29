"""
Atividade 2 — Testes para a classe Calculadora usando unittest.
Para rodar: python test_calculadora.py
"""

import unittest
from calculadora import Calculadora


class TestCalculadora(unittest.TestCase):

    def setUp(self):
        """Cria uma instância da Calculadora antes de cada teste."""
        self.calc = Calculadora()

    # --- Testes de SOMAR ---
    def test_somar_positivos(self):
        self.assertEqual(self.calc.somar(3, 4), 7)

    def test_somar_negativos(self):
        self.assertEqual(self.calc.somar(-2, -8), -10)

    def test_somar_zero(self):
        self.assertEqual(self.calc.somar(5, 0), 5)

    # --- Testes de SUBTRAIR ---
    def test_subtrair_positivos(self):
        self.assertEqual(self.calc.subtrair(10, 3), 7)

    def test_subtrair_resultado_negativo(self):
        self.assertEqual(self.calc.subtrair(2, 9), -7)

    # --- Testes de MULTIPLICAR ---
    def test_multiplicar_positivos(self):
        self.assertEqual(self.calc.multiplicar(4, 5), 20)

    def test_multiplicar_por_zero(self):
        self.assertEqual(self.calc.multiplicar(99, 0), 0)

    def test_multiplicar_negativos(self):
        self.assertEqual(self.calc.multiplicar(-3, -3), 9)

    # --- Testes de DIVIDIR ---
    def test_dividir_normal(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)

    def test_dividir_resultado_decimal(self):
        self.assertAlmostEqual(self.calc.dividir(7, 2), 3.5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
