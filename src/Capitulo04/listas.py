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

#FUNÇÕES BUILTIN-IN PARA TRABALHAR COM LISTAS

lista_numeros = [10, 5, 4 ,7]

#tamanho da lista
len(lista_numeros)

#Pegar o maior numero da lista
max(lista_numeros)

#Pegar o menor número da lista
min(lista_numeros)

lista_nomes = ['Aaron', 'Sabrina', 'duda']

#adicionar mais um elemento na lista, como o append se pode adicionar uma string mais de uma vez e precisa tomar cuidado justamente com isso
lista_nomes.append("Issllany")
lista_nomes.append("Issllany")
print(lista_nomes.count('Issllany'))
print(lista_nomes)

a = []

print(a)
print(type(a))

a.append(3)

print(a)

old_list = [1, 3, 7, 8]
new_list = []

#o item vai percorrer tds os elementos da lista old_list e adicionar na new_list
for item in old_list:
    new_list.append(item)

    print(new_list)