"""
Atividade 2 — Classe Calculadora com somar, subtrair, multiplicar e dividir.
"""


class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida!")
        return a / b
