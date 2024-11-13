lista01 = [1, 2, 3, 4]
lista2 = [5, 6, 7]

for elemento_lista1 in lista01:
    for elemento_lista2 in lista2:
        #multiplica cada valor da lista 2 com o elemento da lista 1
        print(elemento_lista1 * elemento_lista2)

    print('---- \n')


lista3 = [47, 39, 78, 90, 190]
lista4 = [65, 89, 47, 89, 90]

for elemento in lista3:
    for elemento2 in lista4:
        if elemento == 47 and elemento2 == 47:
            print("Achei o 47 nas duas listas!!")
            break
soma = 0
#lista vira uma lista com os elemetos de lista3 e lista4
for lista in [lista3, lista4]:
    for num in lista:
        if num%2 == 0:
            soma += num

print(soma)

#Dá para contatenar as litas assim, ao inves de colocar for dentro de for
lista3 + lista4
soma = 0
for num in lista4+lista3:
    if num%2 == 0:
        soma+=num
print(soma)