"""Lógica do jogo de adivinhação."""

import random
import math


def jogar():
    numero = random.randint(1, 100)
    tentativas = 0

    print("\n🎮 Jogo iniciado! Adivinhe o número entre 1 e 100.")

    while tentativas < 7:
        try:
            chute = int(input("Seu palpite: "))
        except ValueError:
            print("⚠️  Digite um número válido!")
            continue

        tentativas += 1
        distancia = abs(numero - chute)

        if chute == numero:
            print(f"🎉 Acertou em {tentativas} tentativa(s)!")
            return

        direcao = "MAIOR ⬆️" if chute < numero else "MENOR ⬇️"
        print(f"O número é {direcao} | Distância: {distancia} (√ ≈ {round(math.sqrt(distancia), 1)})")

    print(f"💀 Game over! O número era {numero}.")
