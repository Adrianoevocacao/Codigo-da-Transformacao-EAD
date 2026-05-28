"""
Módulo de Utilidades Matemáticas
Contém funções úteis para operações matemáticas.
"""


def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b


def subtracao(a, b):
    """Retorna a subtração de dois números."""
    return a - b


def multiplicacao(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b


def divisao(a, b):
    """Retorna a divisão de dois números."""
    if b == 0:
        return "❌ Erro: divisão por zero não é permitida!"
    return a / b


def potencia(base, expoente):
    """Retorna a potência de um número."""
    return base ** expoente


def media(numeros):
    """Retorna a média de uma lista de números."""
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)
