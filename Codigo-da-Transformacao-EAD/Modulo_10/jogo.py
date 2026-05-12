import random

numero = random.randint(1, 100)

tentativa = int(input("Adivinhe o número de 1 a 100: "))

if tentativa == numero:
    print("Você acertou!")
else:
    print("Você errou!")
    print("O número era:", numero)