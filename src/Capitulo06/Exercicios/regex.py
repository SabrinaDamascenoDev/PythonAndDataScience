import re
texto = 'A Data Science Academy oferece os melhores cursos de análise de dados do Brasil.'

resul = re.findall(r'(?<=Data) \w+', texto)
resul2 = re.findall(r'(?<=Science) \w+', texto)
print(resul[0], resul2[0])