"""
Atividade 1 — Teste da função soma usando unittest.
Para rodar: python test_soma.py
"""

import unittest
from soma import soma


class TestSoma(unittest.TestCase):

    def test_soma_positivos(self):
        """Testa soma de dois números positivos."""
        self.assertEqual(soma(2, 3), 5)

    def test_soma_negativos(self):
        """Testa soma de dois números negativos."""
        self.assertEqual(soma(-1, -4), -5)

    def test_soma_zero(self):
        """Testa soma com zero."""
        self.assertEqual(soma(10, 0), 10)

    def test_soma_floats(self):
        """Testa soma de números decimais."""
        self.assertAlmostEqual(soma(1.5, 2.5), 4.0)

    def test_soma_positivo_negativo(self):
        """Testa soma de número positivo com negativo."""
        self.assertEqual(soma(10, -3), 7)


if __name__ == "__main__":
    unittest.main(verbosity=2)
