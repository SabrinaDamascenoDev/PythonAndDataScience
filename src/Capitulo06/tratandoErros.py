
def askInt():
    try:
        val = int(input("Digite um valor: "))
    except:
        print("Você não digitou um número")
        val = int(input("Digite um valor novamente: "))
    finally:
        print("Obrigada")

askInt()
#Vai ficar repetindo
def askInt2():
    while True:
        try:
            val = int(input("Digite um valor: "))
        except:
            print("Você não digitou um número")
            continue
        else:
            print("Obrigada por digitar um numero")
            break
        finally:
            print("Fim da execução")
        print(val)

askInt2()