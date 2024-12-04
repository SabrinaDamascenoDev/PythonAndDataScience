#Gravando arquivo, se n existir ele cria e se existir ele abre e sobescreve
arq = open('arquivos/arq2.txt', 'w')

arq.write("Aprendendo python")
arq.close()
arq = open('arquivos/arq2.txt', 'r')
print(arq.read())

#append ele adiciona no ja exixtente e n sobreescreve
arq = open('arquivos/arq2.txt', 'a')
arq.write(" Muito bom")

arq = open('arquivos/arq2.txt', 'r')
print(arq.read())

arqSalarios = open('arquivos/arquivos/salarios.csv', 'r')

data = arqSalarios.read()

#dividir qnd encontrar o \n
rows = data.split('\n')

print(rows)

#dividir em colunas
colunas = []

for row in rows:
    elementos = row.split(',') #em=ncontrou uma virgula faz uma divisão
    colunas.append(elementos)

print(colunas)