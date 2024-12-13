#reduz uma lista de elementos a um unico valor

from functools import reduce

lista = [56, 48, 98, 67]

def soma(a, b):
    return a+b

print(reduce(soma, lista))


print(reduce(lambda a, b: a+b, lista))

max_find = lambda x, y: x if x > y else y

#é como se fosse um for que percorre todos os valores da lista e acha o maior, nesse caso ja que a função lambda é para isso
print(reduce(max_find, lista))