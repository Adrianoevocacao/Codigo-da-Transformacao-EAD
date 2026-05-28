"""
Atividade 3 - Jogo de Adivinhação
Usa random para gerar número e math para dicas de distância.
"""

import random
import math

def jogar():
    print("=" * 40)
    print("      JOGO DE ADIVINHAÇÃO 🎮")
    print("=" * 40)
    print("Adivinhe o número entre 1 e 100!\n")

    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 7

    while tentativas < max_tentativas:
        tentativas_restantes = max_tentativas - tentativas
        print(f"🎯 Tentativas restantes: {tentativas_restantes}")

        try:
            chute = int(input("Digite seu palpite: "))
        except ValueError:
            print("⚠️  Digite apenas números!\n")
            continue

        tentativas += 1
        distancia = abs(numero_secreto - chute)

        if chute == numero_secreto:
            print(f"\n🎉 PARABÉNS! Você acertou em {tentativas} tentativa(s)!")
            print(f"O número era: {numero_secreto}")
            break

        # Dica de distância usando math
        if distancia <= 5:
            dica = "🔥 Muito quente! Quase lá!"
        elif distancia <= 15:
            dica = "♨️  Quente! Está perto!"
        elif distancia <= 30:
            dica = "😐 Morno... Continue tentando."
        else:
            dica = "🧊 Frio! Está longe..."

        if chute < numero_secreto:
            print(f"⬆️  O número é MAIOR! {dica}")
        else:
            print(f"⬇️  O número é MENOR! {dica}")

        # Dica matemática de distância com math.sqrt
        raiz = round(math.sqrt(distancia), 2)
        print(f"📐 Distância aproximada: {distancia} (√{distancia} ≈ {raiz})\n")

    else:
        print(f"\n💀 Game over! O número era: {numero_secreto}")

    jogar_novamente = input("\nJogar novamente? (s/n): ").strip().lower()
    if jogar_novamente == "s":
        jogar()
    else:
        print("👋 Obrigado por jogar!")

if __name__ == "__main__":
    jogar()
