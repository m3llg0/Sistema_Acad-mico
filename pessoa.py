import aluno # Sofia
import funcionario_administrativo # Emilly e Lara
import professor # Amelyne e Filipe

class Pessoa: # Melissa
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def info(self):
        print('Informações:')
        print('Nome: ', self.nome)
        print('Idade: ', self.idade)

# instanciando objetos

print('Bem vindo(a) ao Sistema Acadêmico!')
print(' ')

print('Pessoa ')
pessoa01 = Pessoa('João', 15)
Pessoa.info(pessoa01)

print(' ')

print('Aluno ')
aluno01 = aluno.Aluno(1, 'Pedro', 13)
aluno.Aluno.info(aluno01)

print(' ')

print('Funcionário Administrativo ')
funcionario01 = funcionario_administrativo.Funcionario_Administrativo('Julia', 34, 'Secretária')
funcionario_administrativo.Funcionario_Administrativo.info(funcionario01)

print(' ')

print('Professor ')
prof01 = professor.Professor('Biologia', 'Maria', 45)
professor.Professor.info(prof01)