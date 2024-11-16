
valoresA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valoresB = [8, 8, 4, 4]

achei = 0

if len(valoresA) > len(valoresB):
   for i in range(len(valoresB)):
        for j in range(len(valoresA)):
            if valoresB[i] == valoresA[j]:
                achei += 1
                break
else:
    print("A quantidade de valores de A, tem que ser maior que o valor de B.")

if achei == len(valoresB):
    print("Está contido o array B no Array A")
else:
    print("Não está contido o array B no Array A")

