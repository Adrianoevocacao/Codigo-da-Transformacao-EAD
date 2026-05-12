try:

    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    resultado = numero1 / numero2

    print("Resultado:", resultado)

except ZeroDivisionError:

    print("ERRO: não pode dividir por zero!")