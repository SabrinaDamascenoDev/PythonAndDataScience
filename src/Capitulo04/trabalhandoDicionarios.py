
#isso é uma lista, e ela não é uma estrutura ideal para fazer ligações entre informações presentes nela, devido ao fato de que nessa ordem que esta apresentada nada indica que os valores logo apos seguidos dos nomes são a idade dos presentes na lista, por isso existe outra estrutura o dicionario para fazer essa combinação
estudante_lst = ["Pedro", 24, "Ana", 22, "Rolnado", 24, "Janaina", 25]

#isso é um dicionario
estudantes_dic = {"Pedro":24, "Ana":22, "Ronaldo":24, "Janaina":25}
print(estudantes_dic["Pedro"])

#Adiciona esse novo elemento
estudantes_dic["Marcelo"] = 23

print(estudantes_dic)

#limpa o dicionario ou lista
estudantes_dic.clear()
#Deleta o dicionario da memoria
del estudantes_dic

estudantes = {"Sabrina":18, "Maria Eduarda":18, "Issllany Braga":20}

print(len(estudantes))

#Só as chaves, nomes, nesse caso
print(estudantes.keys())

#Só os valores que se conectam as chaves, as idades, nesse caso
print(estudantes.values())

#As chaves e os valores que se conectam a elas
print(estudantes.items())

estudantes2 = {"Joana Paula":19}

#Adiciona dentro do dicionario estudantes os elementos do dicionario estudantes 2
estudantes.update(estudantes2)

#dicionario vazio
dic1 = {}

dic1["Chave01"] = 2

print(dic1)
#vc pode utilizar chaves com diferentes tipos de dados, porem é melhlor utilizar as chaves do mesmo tipo
dic1[9.23] = "Sim"

print(dic1)
dic1["teste"] = 1
dic1["key"] = "teste"

print(dic1)

dic2 = {}

dic2["key1"] = "Ciencia de dados"
dic2["Key2"] = "Analise de dados"
dic2["Key3"] = "Engenharia de dados"

a = dic2["key1"]
b = dic2["Key2"]
c = dic2["Key3"]

print(a, b, c)

dict3 = {"chave1":12, "chave2":["sabs", "sasab"]}

#mudar o que ta no indice 0 da lista para maiusculo
dict3['chave2'][0] = dict3['chave2'][0].upper()
print(dict3["chave2"][0])

dict4 = {"chave1":34,  "chave2":[23, 4, 7, 9]}

#subtrai 2 do 23
dict4['chave2'][0] -= 2

print(dict4['chave2'])

#criando dicionario dentro de dicionario

dict_alinhado = {'key1':{'key2':{'key3':'Python its easy'}}}

print(dict_alinhado)
#conseguir a frase que ta dentro do key3
print(dict_alinhado['key1']['key2']['key3'])

