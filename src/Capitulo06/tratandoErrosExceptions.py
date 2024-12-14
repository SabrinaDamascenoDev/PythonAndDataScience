


def div(a, b):
    if b == 0:
        print("Não podemos dividir por zero")
    else:
        return a / b

a = int(input('Digite algo: '))
b = int(input('Digite algo: '))
print(div(a, b))

try:
    a +'a'
except TypeError:
    print("Operação nao permitida")

try:
    f = open('arquivos/arquivos/testandoerros.txt', 'w')
    f.write('Oi')
except IOError:
    print("Erro: arquivo nao encontrado ou nao pode ser salvo")
else:
    print("Conteudo gravado com sucesso")
    f.close()

try:
    f = open('arquivos/arquivos/testandoerros', 'r')
except IOError:
    print("Erro: arquivo nao encontrado ou nao pode ser salvo")
else:
    print("Conteudo gravado com sucesso")
    f.close()