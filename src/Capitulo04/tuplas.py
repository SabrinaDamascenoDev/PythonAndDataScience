

tupla1 = ("geografia", 23, "Elefante", 9.0, "Python")
print(tupla1)

#Uma estrutura imutável
print(tupla1[0])

print(len(tupla1))
print(tupla1.index("Elefante"))

#converte para lista
lista = list(tupla1)

print(type(tupla1))
print(type(lista))

lista.append("D")
 #altera a lista e converte para tupla again
t2 = tuple(lista)

print(t2)


