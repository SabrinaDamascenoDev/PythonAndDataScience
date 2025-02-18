class Animal:
    def __init__(self):
        print("Animal criado com sucesso!")

    def eat(self):
        print("Animal está comendo")
    def barulho(self):
        pass

class Cachorro(Animal):
    def __init__(self):
        super().__init__()
        print("Cachorro criado com sucesso!")

    def barulho(self):
        print("AuAu")

class Gato(Animal):
    def __init__(self):
        super().__init__()
        print("Gato criado com sucesso!")
    def barulho(self):
        print("Miau Miau")


rex = Cachorro()
rex.barulho()
rex.eat()

