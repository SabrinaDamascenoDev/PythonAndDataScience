#Quando uma função faz parte de uma classe, ela é chamada de método

def primeiraFunc():
    print("Ola, mundo!")

primeiraFunc()

def soma(a, b):
    return a + b

print(soma(5, 10))

def imprimirNumeros():
    for i in range(0, 11):
        print(i)

imprimirNumeros()

def addNumbers(a, b):
    print("The first number is ", a)
    print("The second number is ", b)
    print("A plus B is ", a + b)

addNumbers(76, 89)

#Quando não sei o numero de argumentos que serao passados como param,etro

def printVarInfo(arg1, *vartuple):

    print("O parâmetro passado foi ", arg1)
    for i in  vartuple:
        print("O parâmetro passado foi: ", i)

printVarInfo('Clocolate', 'Pastel', 'Pizza')