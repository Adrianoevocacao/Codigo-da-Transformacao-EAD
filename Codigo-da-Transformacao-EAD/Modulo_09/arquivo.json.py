import json

clientes = {
    "cliente1": {
        "nome": "Adriano",
        "idade": 17
    },
    "cliente2": {
        "nome": "Carlos",
        "idade": 22
    }
}

with open("clientes.json", "w") as arquivo:
    json.dump(clientes, arquivo, indent=4)


with open("clientes.json", "r") as arquivo:
    dados = json.load(arquivo)


print("Dados carregados:")
print(dados)