lista =[2, 3, 4]
listaB = [10, 11, 12]

def potencia(a, b):
    return a ** b

print(list(map(potencia, lista, listaB)))