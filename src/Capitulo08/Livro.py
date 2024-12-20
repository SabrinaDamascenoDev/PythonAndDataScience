class Livro():

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        print("Construtor criado para criar um objeto da classe livro")

    def imprime(self, nome, preco):
        print("Esse é o titulo %s e esse é o preco %d" %(self.nome, self.preco))

Livro2 = Livro("A corte de espinhos e rosas", 40.00)

print(Livro2.imprime("A Corte de espinhos e rosas", 40.0))

print(Livro2.preco)

class Algoritmo():
    def __init__(self, tipo):
        self.tipo = tipo
        print("Construtor concluido")

tipo1 = Algoritmo("Deep Learning")
print(tipo1.tipo)