"""
Atividade 3 — Valida entradas inválidas: divisão por zero deve lançar exceção.
Para rodar: python test_entradas_invalidas.py
"""

import unittest
from calculadora import Calculadora

# Importa a calculadora da atividade 2 — rode a partir da pasta atividade3
# ou copie o calculadora.py para cá também.
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../atividade2"))

from calculadora import Calculadora


class TestEntradasInvalidas(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_divisao_por_zero_lanca_excecao(self):
        """Divisão por zero deve lançar ValueError."""
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

    def test_divisao_por_zero_mensagem(self):
        """Verifica a mensagem de erro da divisão por zero."""
        with self.assertRaises(ValueError) as contexto:
            self.calc.dividir(5, 0)
        self.assertIn("zero", str(contexto.exception).lower())

    def test_divisao_negativo_por_zero(self):
        """Número negativo dividido por zero também lança ValueError."""
        with self.assertRaises(ValueError):
            self.calc.dividir(-8, 0)

    def test_somar_tipos_invalidos(self):
        """Soma de string com número deve lançar TypeError."""
        with self.assertRaises(TypeError):
            self.calc.somar("abc", 5)

    def test_multiplicar_tipo_invalido(self):
        """Multiplicação de None com número deve lançar TypeError."""
        with self.assertRaises(TypeError):
            self.calc.multiplicar(None, 3)

    def test_dividir_resultado_correto_nao_lanca(self):
        """Divisão válida NÃO deve lançar exceção."""
        try:
            resultado = self.calc.dividir(10, 2)
            self.assertEqual(resultado, 5)
        except ValueError:
            self.fail("dividir() lançou ValueError inesperadamente!")


if __name__ == "__main__":
    unittest.main(verbosity=2)
