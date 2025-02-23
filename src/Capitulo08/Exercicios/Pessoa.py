class Pessoa:
    def __init__(self, telefone, nome, idade, cidade, email):
        self.telefone = telefone
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.email = email

    def getTelefone(self):
        return self.telefone
    def toString(self):
        print(f'{self.telefone} {self.nome} {self.idade} {self.cidade} {self.email}')

pessoa01 = Pessoa(999999, "sabrina", 19, "Morada Nova", "algo")
pessoa01.toString()