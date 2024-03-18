class Professor:
    def __init__(self, materia, nome, idade ):
       self.nome = nome
       self.materia = materia
       self.idade = idade

    def info(self):
        print("as informações do professor são: ")
        print("seu nome: ", self.nome)
        print("sua idade é: ", self.idade)
        print("sua matéria é: ", self.materia)