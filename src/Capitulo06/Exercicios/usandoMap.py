palavras = "A data science oferece os melhores cursos de análise de dados do Brasil".split()

resultado = map(lambda w: [w.upper(), w.lower(), len(w)], palavras)
for i in resultado:
    print (i)

