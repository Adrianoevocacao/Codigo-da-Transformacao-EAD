import random
import math


numero_secreto = random.randint(1, 100)

tentativa = int(input("Tente adivinhar o número de 1 a 100: "))


diferenca = math.fabs(numero_secreto - tentativa)

if tentativa == numero_secreto:
    print("Parabéns! Você acertou!")
else:
    print("Você errou!")
    print("O número era:", numero_secreto)
    print("Diferença:", diferenca)