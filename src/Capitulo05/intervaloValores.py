#Intervalo de valores com python



#1-10
for i in range(1, 11):
    print(i)

#0-100, de 2 em 2, só os pares
for i in range(0, 100, 2):
    print(i)

for i in range(0, -20, -2):
    print(i)


lista = ["Abacate", "Uva", "Morango", "Banana"]

lista_tamanho = len(lista)

for i in range(0, lista_tamanho):
    print(lista[i])
