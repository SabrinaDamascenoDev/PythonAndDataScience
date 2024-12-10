import json
import urllib.request
from urllib.request import urlopen

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
dados = json.loads(response)[0]

print(dados)

print(dados['title'])
print(dados['url'])
print(dados['duration'])

arquivo_fonte = 'arquivos/arquivos/dados.json'
arquivo_destino = 'arquivos/arquivos/dados.txt'

with open('arquivos/arquivos/dados.json', 'r') as arquivo:
    texto = arquivo.read()
    with open('arquivos/arquivos/dados.txt', 'w') as arquivoo:
        arquivoo.write(texto)

#forma simplificada

open('arquivos/arquivos/dados.txt', 'w').write(open('arquivos/arquivos/dados.json', 'r').read())

with open('arquivos/arquivos/dados.txt', 'r') as arquivo:
    texto = arquivo.read()
    data = json.loads(texto)

    print(data)