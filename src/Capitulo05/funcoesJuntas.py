import math

def numPrimo(num):
    if(num%2 == 0) and num > 2:
        return "Esse número não é primo"
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if (num%i) == 0:
            return "Esse número não é primo"
    return "É primo"

print(numPrimo(5))

def lowercase(nome):
    return nome.lower()

nomeMeu = "SASASa"
print(lowercase(nomeMeu))