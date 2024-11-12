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


#Funções Bulti-in

#minusculo
print(nome.lower())

#maiusculo
nome.upper()

#quebra a string, vc tbm pode passa como paramentro em qual string vc quer que ele quebre nome.split('b')
nome.split()

#só a primeira letra da frase em maiusculo
nome.capitalize()

#conta quantas vezes a letra 'a' aparece
nome.count('a')

#pergunta se o objeto é td de numeros]
nome.isalnum()

#pergunta se a string ta td minuscula
nome.islower()

#pergunta se a string é toda espaços
nome.isspace()

#pergunta se a string termina com determinada letra
nome.endswith('a')