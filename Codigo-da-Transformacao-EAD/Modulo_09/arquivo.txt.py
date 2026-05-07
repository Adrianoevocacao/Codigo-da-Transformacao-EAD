
arquivo = open("informacoes.txt", "w")

arquivo.write("Nome: Adriano\n")
arquivo.write("Curso: Python\n")
arquivo.write("Cidade: Campinas")

arquivo.close()

# Lendo o arquivo
arquivo = open("informacoes.txt", "r")

conteudo = arquivo.read()

print("Conteúdo do arquivo:")
print(conteudo)

arquivo.close()