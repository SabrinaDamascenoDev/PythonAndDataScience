

valor01 = float(input("Qual o primeiro valor?"))
valor02 = float(input("Qual é o segundo valor?"))
operacao =  int(input("Selecione + - adição, - - subtração, * - multiplicação, / - divisão"))

match operacao:
    case "+":
        print(valor01+valor02)
    case "-":
        print(valor01-valor02)
    case "*":
        print(valor01*valor02)
    case "/":
        print(valor01/valor02)
