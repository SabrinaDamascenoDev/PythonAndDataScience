#precisa colocar int() para converter os valores recebidos para int pq no input recebe so string
largura = int(input("Qual a largura do retangulo?"))
altura = int(input("Qual a altura do retangulo?"))

area_retangulo = largura*altura
perimetro_retangulo = (largura*2)+(altura*2)

print("A área do retangulo é ", area_retangulo)
print("O perimetro do retangulo é ", perimetro_retangulo)
