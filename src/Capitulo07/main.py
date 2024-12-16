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


def game():
    limpa_tela()

    print()