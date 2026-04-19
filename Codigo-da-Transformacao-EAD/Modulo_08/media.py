## Função para calcular média
def calcular_media(notas):
    media = sum(notas) / len(notas)
    if media >= 7:
        print(f"Média: {media:.2f} - Aprovado")
    else:
        print(f"Média: {media:.2f} - Reprovado")