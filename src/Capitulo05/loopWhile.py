
valor = 0
#se não tiver o incremento vai ficar em loop infinito
while valor < 10:
    print(valor)
    valor = valor+1

#pode usar else para parar o while

while valor < 10:
    print("O valor do x é maior que 10, ele é: ", valor)
else:
    print("Loop concluido")

valor = 0
#pass para ele passar para continuar
while valor < 10:
    if valor == 4:
        break
    else:
        pass
    print(valor)
    valor = valor + 1
#se achar z, ele vai passar o z
for letra in "Python é zzz incrivel":
    if letra == "z":
        continue

    print(letra)

#Loop while and for juntos
