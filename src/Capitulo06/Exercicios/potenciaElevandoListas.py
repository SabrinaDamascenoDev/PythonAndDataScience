lista = [2, 3, 4, 5]

def quadrado(a):
    return a ** 2

def cubo(a):
    return a ** 3

def apliInToo(a):
    return quadrado(a), cubo(a)

print(list(map(apliInToo, lista)))