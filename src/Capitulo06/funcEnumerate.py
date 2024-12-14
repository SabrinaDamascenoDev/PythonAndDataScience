lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#indice dos elementos da lista
listaEnumerada = list(enumerate(lista))
print(listaEnumerada)


for indice, valor in listaEnumerada:
    print(indice, valor)

for indice, valor in listaEnumerada:
    if indice >= 2:
        break
    else:
        print(valor)

for indice, valor in enumerate('Data Science Academy'):
    print(indice, valor)


for indice, valor in enumerate(range(10)):
    print(indice, valor)