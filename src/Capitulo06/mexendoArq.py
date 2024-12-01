f = open('arquivos/arquivos/salarios.csv', 'r')

arq = f.read()

rows = arq.split('\n')

full_data = []

for row in rows:
    elemnetos = row.split(",")
    full_data.append(elemnetos)

#numero de linhas do arquivo
count = 0
for elemento in full_data:
    count += 1

print(count)


arq = open('arquivos/arquivos/salarios.csv', 'r')
arqEle = arq.read()
rowsAll = arqEle.split('\n')
full_datas = []

for row in rowsAll:
    elemnetos = row.split(",")
    full_datas.append(elemnetos)
    first_elemento = full_datas[0]

print(first_elemento)

countCol = 0
for element in first_elemento:
    countCol +=1

print(countCol)

info = open('arquivos/arq3.txt', 'w')

info.write("Só testando para criar esse arquivo")

infor = open('arquivos/arq3.txt', 'a')

infor.write(' \n  viu \n viu ')
infors = open('arquivos/arquivos/arquivo3.txt', 'r')
print(infors.readlines())


for row in open('arquivos/arquivos/arquivo3.txt'):
    print(row)