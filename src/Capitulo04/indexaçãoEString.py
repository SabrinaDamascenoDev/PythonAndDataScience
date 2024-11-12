nome = "Sabrina"
sobrenome = "Rabelo"

nomeCompleto = nome + " " + sobrenome

print(nome[0])

#FATIAMENTO SEM ALTERAR O VALOR PRINCIPAL
#todos os elementos atras do elemento de indice 2, ou seja, o 0 e 1
print(nome[:2])

#todos os elementos apos o indice 4, ou seja, 5, 6 e 7
print(nome[4:])

#mostra o ultimo elemento
print(nome[-1])

#mostra os tres primeiros numeros, tirando os 4 ultimos
print(nome[:-4])

#traz as letras de 2 em 2
print(nome[::2])

#String é um valor imutavel, n pode alterar algum elemento da string

#multiplica a string
letra = 's'

print(letra*2)