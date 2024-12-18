#Jogo da forca
import random
from os import system, name

def limpa_tela():
    #Windows
    if name == 'nt':
        _= system('cls')
    # Mac ou linux
    else:
        _= system('clear')

def display_hangman(chances):
    stages = [
        '''
            ----------
            |        | 
            |        0
            |       
            |           
            |        
            -
        ''',
        '''
             ----------
             |        | 
             |        0
             |        |
             |           
             |        
             -
        ''',
        '''
             ----------
             |        | 
             |        0
             |        | 
             |        |  
             |        
             -
        ''',
        '''
             ----------
             |        | 
             |        0
             |       \|
             |        |   
             |        
             -
        ''',
        '''
             ----------
             |        | 
             |        0
             |       \|/ 
             |        |   
             |        
             -
        ''',
        '''
            ----------
            |        | 
            |        0
            |       \|/ 
            |        |   
            |       / 
            -
        ''',
        '''
            ----------
            |        | 
            |        0
            |       \|/ 
            |        |   
            |       / \\
            -
        '''

    ]
    return stages[chances]
def game():

    limpa_tela()

    print("\nBem-vindo(a) ao jogo da forca! \nAdivinhe a palavra abaixo:\n")

    #Listas de palavras
    palavras = ["banana", "uva", "abacati", "morango", "melancia"]
    palavra = random.choice(palavras)

    chances = 6
    letras_erradas = []
    naoAchou = 0
    linhasDescobertas = []




    for i in palavra:
        linhasDescobertas.append("_")
    while chances > 0:

        print(display_hangman(chances))
        print(" ".join(linhasDescobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas: ", len(letras_erradas))

        tentativa = input("\nDigite uma letra:")

        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    linhasDescobertas[index] = letra
                index+=1
        else:
            letras_erradas.append(tentativa)
            chances -= 1

        count =0
        for i in linhasDescobertas:
            if i != "_":
                count+=1

        if count == len(palavra):
            print("Parabéns, você acertou!")
            break

    if count != len(palavra):
        print(display_hangman(chances))
        print("\nVocê perdeu, a palavra era: ", palavra)


if __name__ == "__main__":
    game()