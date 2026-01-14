class Livro():
    def __init__(self, titulo: str, autor: str, codigo: str, disponivel: bool):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponivel = disponivel


# Instancia
livro1 = Livro("Memorias Postumas", "Machado de Assis", 1, True)
print(livro1)
