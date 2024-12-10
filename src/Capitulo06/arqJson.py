import json
dict_guido = {'nome':"guido Van Rossum",
              "Linguagem" : "Python",
              "Similar": ["C", "Modula-3", "lisp"],
              "users" : 10000}

for k, v in dict_guido.items():
    print(k, v)

#Converter dicionario em arquivo json, a organização do json é igual o dicionario em chaves e valor
json.dumps(dict_guido)
print(json.dumps(dict_guido))

with open ('arquivos/arquivos/dados.json', 'w') as arq:
    arq.write(json.dumps(dict_guido))

with open('arquivos/arquivos/dados.json', 'r') as arq:
    texto = arq.read()
    #carrega o conteudo do texto em json
    dados = json.loads(texto)

#imprime o dado ligado a chave nome
print(dados['nome'])