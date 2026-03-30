##Lista de compras Adicionar/remover##

lista = []

while True:
    print("\n1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Ver lista")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        item = input("Digite o item: ")
        lista.append(item)

    elif opcao == "2":
        item = input("Digite o item para remover: ")
        if item in lista:
            lista.remove(item)
        else:
            print("Item não encontrado")

    elif opcao == "3":
        print("Lista:", lista)

    elif opcao == "4":
        break

##Dicionário do aluno##

aluno = {
    "nome": "João",
    "idade": 16,
    "notas": [8, 7.5, 9]
}

print("\nDados do aluno:")
print("Nome:", aluno["nome"])
print("Idade:", aluno["idade"])
print("Notas:", aluno["notas"])

#Números pares e ímpares##

numeros = [1, 2, 3, 4, 5, 6, 7, 8]

pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("Pares:", pares)
print("Ímpares:", impares)