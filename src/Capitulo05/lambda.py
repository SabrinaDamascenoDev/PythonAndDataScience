#Simplificando funcoes ->
def potencia(num):
    potenciaa = num ** 2
    return potencia

def potencia2(num):
    return num ** 2

def potencia3(num): return num ** 2

#Função anonima
potencia4 = lambda num: num ** 2

print(potencia4(4))

first = lambda x: x[0]

print(first("Sabrina"))

reverse = lambda x: x[::-1]
print(reverse("Sabrina"))

sum = lambda x, y: x + y
print(sum(1,2))