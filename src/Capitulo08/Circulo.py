class Circulo:

    def __init__(self, raio=5):
        self.raio = raio

    def area(self):
        return 3.14 * (self.raio ** 2)

    def setRaio(self, novoRaio):
        self.raio = novoRaio

    def getRaio(self):
        return self.raio