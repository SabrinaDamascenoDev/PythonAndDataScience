#listas com strings
lista_1 = ['sabrina', 'duda', 'issllany']

lista_2 = [1, 2, "sabrina"]


item1 = lista_2[0]
item2 = lista_2[1]
item3 = lista_2[2]

print(lista_2[2])
lista_2[2] = "duda"
print(lista_2[2])
#deletar elemento
del lista_2[1]

print(lista_2)

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


print(listas)

b = listas[0]
print(b)

#o numero 2 esta dentro da lista?
print(2 in b)

valorInicial = b[0]
print(valorInicial)

a = listas[0][0]

print(a)

listas_totais = listas + b

print(listas_totais)