try:

    idade = int(input("Digite sua idade: "))

    if idade < 0:
        print("Idade inválida!")

    else:
        print("Idade válida!")

except ValueError:

    print("ERRO: digite apenas números!")