
def numeroPar(a):
    if a % 2 == 0:
        return True
    else:
        return False


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list((filter(numeroPar, lista))))

print(list(filter(lambda x: x % 2 == 0, lista)))