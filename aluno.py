class Aluno:
    def __init__(self, matricula, nome, idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade

    def info(self):
        print("As informações é: " )
        print('Seu nome: ', self.nome)
        print('Sua idade é: ', self.idade)
        print('Sua matricula é: ', self.matricula)
