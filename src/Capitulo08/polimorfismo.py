class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def frear(self):
        pass
    def acelerar(self):
        pass

class Carro(Veiculo):
    def frear(self):
        print("Carro freando")
    def acelerar(self):
        print("Carro acelerando")

class Bicicleta(Veiculo):
    def frear(self):
        print("Bicicleta freando")
    def acelerar(self):
        print("Bicicleta acelerando")
    def pilotar(self):
        print("Bicicleta pilotar")

newBic = Bicicleta("sim", "algum")
newBic.frear()

lista_veirculos = [Carro("Porshe", 567), Bicicleta("Bic", 345)]
for item in lista_veirculos:
    print(item.marca, item.modelo)
    item.acelerar()
    if isinstance(item, Bicicleta):
        item.pilotar()