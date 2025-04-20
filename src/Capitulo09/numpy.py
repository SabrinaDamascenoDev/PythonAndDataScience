import numpy as np

#Array com o Numpy, a partir de uma lista
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr1)
print(type(arr1))
# Só uma dimenção (3,); com duas (2, 3); com três (4, 3, 2)
print(arr1.shape)

#Do index 1 ate o 4
print(arr1[1:5])

#Criar maskara
mask = (arr1%2 == 0)
print(mask)
print(arr1[mask])

try:
    arr1[0] = 'oi'
except:
    print("Operação não permitida")