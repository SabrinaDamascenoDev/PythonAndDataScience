#O que são expressões regulares?  São expressões usadas para combinar ou encontrar ocorrencias de sequencias de caractere em uma string
import re

texto = "Meu email é exemplo@gmail.com e voce pode conectar outro_email@gmail.com"
resultado = len(re.findall('@', texto))
print(resultado)

#a palavra depois do voce no texto
resul = re.findall(r'voce (\w+)', texto)
print(resul[0])

texto2 = "Isso é incrivelmente perdido, mas se encontra rapidamente"
for match in re.finditer(r"\w+mente\b", texto2):
    print("%02d-%02d: %s" % (match.start(), match.end(), match.group(0)))

