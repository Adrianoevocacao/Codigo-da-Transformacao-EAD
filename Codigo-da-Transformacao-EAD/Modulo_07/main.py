"""
Programa Principal - Atividade 1
Importa e utiliza o módulo utilidades.py
"""

import utilidades

print("=" * 40)
print("   CALCULADORA COM MÓDULO PRÓPRIO")
print("=" * 40)

print(f"\n➕ Soma de 10 + 5        = {utilidades.soma(10, 5)}")
print(f"➖ Subtração de 10 - 3   = {utilidades.subtracao(10, 3)}")
print(f"✖️  Multiplicação de 4x6  = {utilidades.multiplicacao(4, 6)}")
print(f"➗ Divisão de 20 / 4     = {utilidades.divisao(20, 4)}")
print(f"🔢 Potência de 2^10      = {utilidades.potencia(2, 10)}")
print(f"📊 Média de [5,10,15,20] = {utilidades.media([5, 10, 15, 20])}")

print("\n✅ Módulo utilidades importado e utilizado com sucesso!")
