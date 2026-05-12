class Livro:

    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor
        self.emprestado = False


class Biblioteca:

    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def mostrar_livros(self):

        for livro in self.livros:

            if livro.emprestado == False:
                status = "Disponível"
            else:
                status = "Emprestado"

            print(livro.nome, "-", livro.autor, "-", status)

    def emprestar_livro(self, nome_livro):

        for livro in self.livros:

            if livro.nome == nome_livro:

                if livro.emprestado == False:
                    livro.emprestado = True
                    print("Livro emprestado com sucesso!")

                else:
                    print("Livro já está emprestado!")


livro1 = Livro("Harry Potter", "J.K Rowling")
livro2 = Livro("Percy Jackson", "Rick Riordan")

biblioteca = Biblioteca()

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

biblioteca.mostrar_livros()

print()

biblioteca.emprestar_livro("Harry Potter")

print()

biblioteca.mostrar_livros()