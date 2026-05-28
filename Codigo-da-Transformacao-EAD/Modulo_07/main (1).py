"""
Desafio Extra - Projeto Organizado em Pacotes
Importa e usa os três pacotes: calculadora, gerador, jogo.
"""

from calculadora import soma, subtracao, multiplicacao, divisao, potencia
from gerador import gerar_pessoa, gerar_data
from jogo import jogar

print("=" * 45)
print("   PROJETO ORGANIZADO EM PACOTES 📦")
print("=" * 45)

# --- Pacote Calculadora ---
print("\n📐 CALCULADORA:")
print(f"  5 + 3      = {soma(5, 3)}")
print(f"  10 - 4     = {subtracao(10, 4)}")
print(f"  6 x 7      = {multiplicacao(6, 7)}")
print(f"  20 / 4     = {divisao(20, 4)}")
print(f"  2 ^ 8      = {potencia(2, 8)}")

# --- Pacote Gerador ---
print("\n👤 GERADOR DE DADOS:")
pessoa = gerar_pessoa()
for chave, valor in pessoa.items():
    print(f"  {chave.capitalize()}: {valor}")
print(f"  Data/Hora: {gerar_data()}")

# --- Pacote Jogo ---
print("\n🎮 JOGO DE ADIVINHAÇÃO:")
jogar()
