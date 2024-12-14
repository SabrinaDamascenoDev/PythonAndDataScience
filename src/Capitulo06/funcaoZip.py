
# Agrupa elementos de multiplas estruturS

listaA = [1, 2, 3, 4, 5]
listaB = [6, 7, 8, 9, 10]

juntas = list(zip(listaA, listaB))

# fica em tuplas agrupados assim oh [(1, 6), (2, 7)]
print(juntas)

# ela só junta a quatidade igual dos dois elementos, se tiver uma lista de 4 elementos e outra de 2 ent só vai ter 2 tuplas

print(list(zip('ABCD', 'xy')))

dic1= {'c1': 1, 'c2': 2, 'c3': 3}
dic2 = {'c4': 4, 'c5': 5}

#Ele combina as chaves, sem os valores
print(list(zip(dic1, dic2)))

#Com o metodo values bpuxa os valores
print(list(zip(dic1, dic2.values())))

def trocaValores(a, b):
    valores = {}

    for d1key, d2Val in zip(a, b.values()):
        valores[d1key] = d2Val

    print(valores)

trocaValores(dic1, dic2)