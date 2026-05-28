"""
Desafio Extra — Sistema de Biblioteca
Classes Livro e Biblioteca para gerenciar empréstimos.
"""

from datetime import datetime


class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True

    def __str__(self):
        status = "✅ Disponível" if self.disponivel else "❌ Emprestado"
        return f"📖 '{self.titulo}' — {self.autor} | {status}"

    def __repr__(self):
        return f"Livro(titulo='{self.titulo}', autor='{self.autor}', isbn='{self.isbn}')"


class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []
        self.emprestimos = []

    def adicionar_livro(self, livro):
        """Adiciona um livro ao acervo."""
        self.livros.append(livro)
        print(f"📚 Livro '{livro.titulo}' adicionado ao acervo!")

    def emprestar_livro(self, isbn, nome_usuario):
        """Realiza o empréstimo de um livro pelo ISBN."""
        for livro in self.livros:
            if livro.isbn == isbn:
                if livro.disponivel:
                    livro.disponivel = False
                    emprestimo = {
                        "livro": livro.titulo,
                        "usuario": nome_usuario,
                        "data": datetime.now().strftime("%d/%m/%Y %H:%M")
                    }
                    self.emprestimos.append(emprestimo)
                    print(f"✅ '{livro.titulo}' emprestado para {nome_usuario}!")
                else:
                    print(f"❌ '{livro.titulo}' já está emprestado.")
                return
        print(f"❌ Livro com ISBN {isbn} não encontrado.")

    def devolver_livro(self, isbn):
        """Realiza a devolução de um livro pelo ISBN."""
        for livro in self.livros:
            if livro.isbn == isbn:
                if not livro.disponivel:
                    livro.disponivel = True
                    print(f"🔄 '{livro.titulo}' devolvido com sucesso!")
                else:
                    print(f"⚠️  '{livro.titulo}' já estava disponível.")
                return
        print(f"❌ Livro com ISBN {isbn} não encontrado.")

    def listar_livros(self):
        """Lista todos os livros do acervo."""
        print(f"\n📚 ACERVO — {self.nome}")
        print("=" * 50)
        if not self.livros:
            print("  Nenhum livro cadastrado.")
        for livro in self.livros:
            print(f"  {livro}")
        print("=" * 50)

    def listar_emprestimos(self):
        """Lista o histórico de empréstimos."""
        print(f"\n📋 HISTÓRICO DE EMPRÉSTIMOS — {self.nome}")
        print("=" * 50)
        if not self.emprestimos:
            print("  Nenhum empréstimo realizado.")
        for e in self.emprestimos:
            print(f"  📖 '{e['livro']}' → {e['usuario']} em {e['data']}")
        print("=" * 50)


# --- Testando o sistema ---
biblioteca = Biblioteca("Biblioteca Central")

# Adicionando livros
livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "ISBN-001")
livro2 = Livro("Python Fluente", "Luciano Ramalho", "ISBN-002")
livro3 = Livro("Clean Code", "Robert C. Martin", "ISBN-003")

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

# Listando acervo
biblioteca.listar_livros()

# Realizando empréstimos
print("\n📤 EMPRÉSTIMOS:")
biblioteca.emprestar_livro("ISBN-001", "Ana Silva")
biblioteca.emprestar_livro("ISBN-002", "Carlos Souza")
biblioteca.emprestar_livro("ISBN-001", "João Lima")  # já emprestado

# Listando acervo após empréstimos
biblioteca.listar_livros()

# Devolvendo livro
print("\n📥 DEVOLUÇÕES:")
biblioteca.devolver_livro("ISBN-001")

# Acervo final
biblioteca.listar_livros()

# Histórico
biblioteca.listar_emprestimos()
