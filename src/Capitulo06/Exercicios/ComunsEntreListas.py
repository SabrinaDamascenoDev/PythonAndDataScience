lista = [1,2,3,5,7,9]
listab = [2,3,5,6,7,8]

resul = filter(lambda x: x in listab, lista)
print(list(resul))