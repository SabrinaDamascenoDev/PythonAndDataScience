#ifs

if 5 > 2:
    print("Its true, bebe")
else:
    print("Its not, bebe")

dia = "Terca"

if dia == "segunda":
    print("Hoje é segunda")
else:
    print("hj é terça")


if dia == "Segunda":
    print("Hoje é segunda")
elif dia == "Terca":
    print("Hoje é terça")
else:
    print("Não é nenhum dos dois dias")


hora = 15

if dia == "Terca" and hora == 12:
    print("Certo")
else:
    print("Errado")


if dia == "Terca" or hora == 12:
    print("Certo")
else:
    print("Errado")

# %r para int e %s para string
if dia == "Terca" and hora != 12:
    print("O dia hoje é %s com hora igual %r" %(dia, hora))
else:
    print("Errado")