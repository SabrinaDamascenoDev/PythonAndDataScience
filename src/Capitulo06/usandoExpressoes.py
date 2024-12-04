#com o with n precisa usar o close()
with open('arquivos/arquivos/cientista.txt', 'r') as arquivos:
    conteudo = arquivos.read()

print(len(conteudo))
print(conteudo)

with open('arquivos/arquivos/cientista.txt', 'w') as arquivos:
    arquivos.write(texto[:19])
    arquivos.write('\n')
    arquivos.write(texto[28:66])

sim = open('arquivos/arquivos/cientista.txt', 'r')
cont = sim.read()
sim.close()
print(cont)
