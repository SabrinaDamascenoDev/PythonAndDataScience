class Livro():

    #Metodo construtor
    def __init__(self):
        self.titulo = 'Sapiens - Uma breve história da humanidade'
        self.isbn = 998888
        print("Construtor chamado para criar um objeto dessa classe")

    def imprime(self):
        print("Foi criado o livro %s ISBN %d" %(self.titulo, self.isbn))

Livro1 = Livro()
Livro1.imprime()
print(Livro1.titulo)