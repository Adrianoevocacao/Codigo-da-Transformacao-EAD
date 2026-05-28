
#Operações matemáticas

num1 = float(input("Digite o primeiro numero:  "))
num2 = float(input("Digite o segundo numero:  "))


print("Soma:", num1 + num2)
print("Subtração:", num1 - num2)
print("Mutiplicação:", num1 * num2)
print("Divisão:", num1 / num2)

#Mostrar qual número é maior 

num1um1 = float(input("Digite o primeiro numero:  "))
num2 = float(input("Digite o segundo numero:  "))

if num1 > num2:
    print("O maior número é:", num1)
elif num2 > num1:
    print("O maior número é:", num2)
else:
    print("Os números são iguais")

#Clasificação por idade 

idade = int(input("Digite sua idade:"))

if idade <=12:
    print("Criança")
elif idade <=17: 
    print("Adolescente")
elif idade <= 59: 
    print("adulto")
else:
    print("idoso")          