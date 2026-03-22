print ("Calculadora simples")

num1 = float(input("Digite o primeiro numero:  "))
num2 = float(input("Digite o segundo numero:  "))

operaçao = input("Escolha a operação (+, -, *, /): ")


if operaçao == "+":
    resultado = num1 + num2
elif operaçao == "-":
    resultado = num1 - num2 
elif operaçao == "*":
    resultado = num1 * num2
elif operaçao == "/":
    resultado = num1 / num2 
else:
    print("operação invalida")
    resultado = None 

if resultado != None:
    print("Resultado:", resultado)              

