import os
texto = "Data Science é muito muito lçegal. \n"
texto = texto + "Eu adoro muito o curso do Data Science Academy. \n"
texto += "Demais mesmo."


arq = open(os.path.join('arquivos/arquivos/cientista.txt'), 'w')

#Split sem nada nos () quebra a frase em tds os espaços
for palavra in texto.split():
    arq.write(palavra + ' ')

arq.close()

arq = open('arquivos/arquivos/cientista.txt', 'r')

conteudo = arq.read()
arq.close()
for frase in conteudo.split('.'):
    print(frase)