#Calculadora em Python

def sum(num1, num2):
    return num1+num2
def sub(num1, num2):
    return num1-num2
def mult(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1 / num2

print("*********** Calculadora em Python *********** \n "
      "Selecione o número da operação desejada: \n"
      "1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n")

operacao = int(input("Digite sua opção (1/2/3/4): "))

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

#Não da para concatenar um int com uma string, tem que deixar td str pra printar usando o str()
match operacao:
    case 1:
        resul = sum(num1, num2)
        print(str(num1) + " + " + str(num2) + " = " + str(resul))
    case 2:
        resul = sub(num1, num2)
        print(str(num1) + " - " + str(num2) + " = " + str(resul))
    case 3:
        resul = mult(num1, num2)
        print(str(num1) + " * " + str(num2) + " = " + str(resul))
    case 4:
        resul = div(num1, num2)
        print(str(num1) + " / " + str(num2) + " = " + str(resul))


