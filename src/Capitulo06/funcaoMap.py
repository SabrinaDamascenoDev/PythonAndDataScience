#A função map aplica uma determinada funcao a cada item de uma sequecia, como lista, dicionaroio e retorna a sequecia de resultados



def potencia(x):
    return x**2

numeros = [1, 2, 3, 4, 5]

#Chama a def funcao para tds os numeros da lista numeros e converte o resultado em uma lista
numerosAoQuadrado = list(map(potencia, numeros))

def fahrenheitt(c):
    return c * 9 / 5 + 32

def celsius(f):
    return f - 32

temp = [93, 243, 545, 546]

print(list(map(fahrenheitt, temp)))

print(numerosAoQuadrado)

for temperatuda in map(fahrenheitt, temp):
    print(temperatuda)

for temperatuda in map(celsius, temp):
    print(temperatuda)

print(map(lambda x: (5.0/9)*(x-32), temp))

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

print(list(map(lambda x, y : x+y, a, b)))

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = [5, 6, 7, 8]

print(list(map(lambda x, y, q: x+y+q, a, b, c)))