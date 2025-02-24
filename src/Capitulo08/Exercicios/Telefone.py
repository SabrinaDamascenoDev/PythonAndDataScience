class Telefone:
    def __init__(self, interface, tamanho):
        self.interface = interface
        self.tamanho = tamanho

class MP3Layer(Telefone):
    def __init__(self, interface, tamanho):
        super().__init__(interface, tamanho)
        self.capacidade = 100
    def usarCapacidade(self, usado):
        self.capacidade -= usado
        if self.capacidade <= 0:
            self.capacidade = 0
            print("Sua capacidade acabou!!")
        else:
            print("Sua capacidade é " + str(self.capacidade) + " !!")

obj = MP3Layer("Samsung", 6.45)
obj.usarCapacidade(80)