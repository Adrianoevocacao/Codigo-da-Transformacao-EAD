import csv

notas = [
    ["Nome", "Nota"],
    ["Adriano", 8.5],
    ["Maria", 9.0],
    ["João", 7.5]
]

with open("notas.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)

    for linha in notas:
        escritor.writerow(linha)

with open("notas.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)

    print("Notas dos alunos:")
    
    for linha in leitor:
        print(linha)