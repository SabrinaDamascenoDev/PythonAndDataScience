itens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print([item for item in itens if (item > 3)])

#retorn x para cada x na lista 0 - 10
print([x for x in range(10)])

#return x para cada num x de 0, 10 que é menor que 5
list_num = [x for x in range(10) if x < 5]
print(list_num)

lista_frutas = ["Banana", "Abacaxi", "Melancia", "Manga"]

lista_novas = []
for x in lista_frutas:
    if "M" in x:
        lista_novas.append(x)

print(lista_novas)

nova_lista = [x for x in lista_frutas if "M" in x]

print(nova_lista)

dict_alunos = {"Gabriel": 23, "Sabrina": 18}

nomes_alunos = {k:v for (k, v) in dict_alunos.items()}
print(nomes_alunos)

aprovas = {k: "Aprovado" if v > 20 else "Reprovado" for k, v in dict_alunos.items()}
print(aprovas)