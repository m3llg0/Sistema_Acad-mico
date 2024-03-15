class Funcionario_Administrativo:
    def __init__ (self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo

    def info(self):
        print("As informações do Funcionário são: ")
        print("Seu nome: ", self.nome)
        print("Sua idade: ", self.idade)
        print("Seu cargo: ", self.nome)