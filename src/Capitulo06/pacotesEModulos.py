#Modulo é um script q contem codigo python e pode ser importado em outros arquivos python
# Ele é usado para compartilhar funções, classes e variaveis
#Já um pacote é uma coleção de módulos que são organizados em uma estrututra de diretórios

from numpy import sqrt
import random
import statistics
import os
import urllib.request

print(sqrt(12))

#Explica como funciona o modulo sqrt do pacote numpy
print(help(sqrt))

print(random.choice(['laranja', 'maca', 'banana']))

print(random.sample(range(100), 10))

dados = [4, 5, 6, 7, 4, 4, 657, 4, 5, 45, 35, 847]

#media de dados
statistics.mean(dados)
#mediana dos dados
statistics.median(dados)

print(help(os))

print(os.getcwd())

resposta = urllib.request.urlopen('http://www.python.org')

html = resposta.read()

print(resposta)

print(html)
