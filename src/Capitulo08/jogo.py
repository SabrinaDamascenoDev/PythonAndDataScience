
import random
from os import system, name

def limpa_tela():
    #Windows
    if name == 'nt':
        _= system('cls')
    # Mac ou linux
    else:
        _= system('clear')


board = [
    '''
    >>>>>>>>>>Hangman<<<<<<<<<<

    +---+
    |   |
        |
        |
        |
        |
    =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''

     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========''', '''

     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========''', '''

     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========''', '''

     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    '''
]



class Hangman:
    def __init__(self, palavra):
        self.palavra = palavra
        self.letrasErradas = []
        self.letrasDescobertas = []
        self.chances = 6

    # Verificar se a palavra digitada é correta ou não e adicionar em suas respectivas listas
    def guess_letter(self, letra):
        if letra in self.palavra and letra not in self.letrasDescobertas:
            self.letrasDescobertas.append(letra)
        elif letra not in self.palavra and letra not in self.letrasErradas:
            self.letrasErradas.append(letra)
        else:
            return False
        return True
    def hangman_over(self):
        return self. hangman_won() or (len(self.letrasErradas) == 6)

    def hangman_won(self):
        if '_' not in self.hide_palavra():
            return True
        return False
    def hide_palavra(self):
        rtn = ''

        for letra in self.palavra:
            if letra not in self.letrasDescobertas:
                rtn += '_'
            else:
                rtn += letra
        return rtn
    def status_game(self):
        print(board[len(self.letrasErradas)])

        print('\nPalavra:' + self.hide_palavra())

        print('Letras erradas: ',)
        for letra in self.letrasErradas:
            print(letra, end=' ')

        print('\nLetras descobertas: ',)
        for letra in self.letrasDescobertas:
            print(letra, end=' ')
        print()


def rand_palavra():
    palavras = ["banana", "uva", "abacati", "morango", "melancia"]

    palavra = random.choice(palavras)

    return palavra


def main():

    limpa_tela()

    game = Hangman(rand_palavra())
    while not game.hangman_over():

        game.status_game()

        user_input = input('\nDigite uma letra: ')
        game.guess_letter(user_input)

    game.status_game()
    if game.hangman_won():
        print('Parabéns')
    else:
        print('Game over')
        print('A palavra era' + game.palavra)




if __name__ == '__main__':
    main()


