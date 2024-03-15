class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def info(self):
        print('Informações:')
        print('Nome: ', self.nome)
        print('Idade: ', self.idade)