import csv

with open('arquivos/arquivos/numeros.csv', 'w') as arquivo:
    #cria o objeto de gravação
    writer = csv.writer(arquivo)

    # Grava no arquivo de linha
    writer.writerow(('nota1', 'nota2', 'nota3'))
    writer.writerow((34, 54, 54))
    writer.writerow((61, 56, 78))
    writer.writerow((67, 89, 98))

#Para leitura indicando que o \n é quebra linha
with open('arquivos/arquivos/numeros.csv', 'r', encoding='utf8', newline='\r\n') as arquivo:
    #Cria o objeto de leitura, gera uma lista
    leitor = csv.reader(arquivo)
    #Percorre cada objeto, linha e imprime
    for x in leitor:
        print(x)

with open('arquivos/arquivos/numeros.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)
    print(dados)

    #Sem o elementto do indice 0, o cabeçalho
    for linha in dados[1:]:
        print(linha)