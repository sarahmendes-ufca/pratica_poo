from livros import Livro
from usuarios import Usuario

class Emprestimo():
    def __init__(self, livro: Livro, usuario: Usuario, ativo: bool):
        self.livro = livro
        self.usuario = usuario
        self.ativo = ativo
    
    def criar_emprestimo(self):
        pass

    def devolver(self):
        pass
