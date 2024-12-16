lista = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

def negativos(num):
    if num < 0:
        return num


print(list(filter(negativos, lista)))