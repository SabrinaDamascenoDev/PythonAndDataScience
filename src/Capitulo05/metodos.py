#Lista vira um objeto, e ele herda diversos metodos ao ser criado que são os que aparecem após o .
lista = [100, -2, 15, 65, 0]

#remove() é um metodo
lista.remove(-2)
print(lista)

lista.append(19)
print(lista)

lista.sort()
print(lista)

print(lista.count(100))

#Mostra oq o metodo faz
help(lista.count)

#Mostra todos os metodos que estao disponiveis para serem usados com esse objeto
print(dir(lista))

#Metodo para quebrar a frase em palavras
nome = "Sabrina Rabelo Damasceno"

print(nome.split())

listaNum = [13, 765, 889, 84, 0, 2]

for i in range(0,len(listaNum)):
    for j in range(0,len(listaNum)):
        #variavel que guarda o valor do indice tal pra trocar, caso preciso dentro do if
        temp = listaNum[i]
        if listaNum[i] < listaNum[j]:
            listaNum[i] = listaNum[j]
            listaNum[j] = temp


print(listaNum)
