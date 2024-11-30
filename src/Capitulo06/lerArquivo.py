arq1 = open("arquivos/arquivo1.txt", "r") # r = read
#vai fazer a leitura impreimir o arquivo
print(arq1.read())

#contar o numero de caracteres
print(arq1.tell())
#quando vc chama dnv o cursor do interpretador vai para o final do conteudo do arquivo
#oq vai mostrar que não tem nada qnd chamar dnv por isso precisa usar de outro jeito
print(arq1.read())

print(arq1.seek(0, 0))

print(arq1.read())
