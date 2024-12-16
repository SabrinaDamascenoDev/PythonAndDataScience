matrix =  [[1, 2], [3, 4], [5, 6], [7, 8]]

for i in matrix:
    for j in range(len(i)):
        temp = i[j]
        i[j] = i[j+1]
        i[j+1] = temp
        break

print(matrix)