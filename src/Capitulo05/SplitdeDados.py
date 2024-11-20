#Vai fatiar a string onde tiver " " espaço
def split_dados(dados):
    return dados.split(" ")

texto = "Meu nome é Sabrina Rabelo Damasceno"

dados = split_dados(texto)
print(dados)

def split_texto_letras(texto):
    texto.upper()
    for letra in texto:
        print(letra)

split_texto_letras(texto)
