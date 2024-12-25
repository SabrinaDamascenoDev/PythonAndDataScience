#Tudo em python é um objeto


class Funcionario:
    def __init__(self, cargo, idade, nome):
        self.cargo = cargo
        self.idade = idade
        self.nome = nome

        print(self.cargo, self.idade, self.nome)

nome1 = input('Digite seu nome: ')
idade1 = input('Digite sua idade: ')
cargo1 = input('Digite seu cargo: ')


