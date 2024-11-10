

valor01 = float(input("Qual o primeiro valor?"))
valor02 = float(input("Qual é o segundo valor?"))
operacao =  input("Selecione + - adição, - - subtração, * - multiplicação, / - divisão")

match operacao:
    case "+":
        print(valor01+valor02)
    case "-":
        print(valor01-valor02)
    case "*":
        print(valor01*valor02)
    case "/":
        print(valor01/valor02)

if operacao == "+":
    resultado = valor02+valor01
    print(resultado)
elif operacao == "-":
    resultado = valor01-valor02
    print(resultado)
elif operacao == "*":
    resultado = valor01*valor02
    print(resultado)
elif operacao == "/":
    resultado = valor01/valor02
    print(resultado)
else:
    print("Valor inválido");