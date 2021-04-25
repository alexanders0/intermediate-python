import random
import os
from unidecode import unidecode


IMAGES = ['''
    You have the power to save the man!

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''
    Hi guy. Can you save me, please?

    +---+
    |   |
    \U0001F600  |
        |
        |
        |
        =========''', '''
    Think about the letters can be repeated!

    +---+
    |   |
    \U0001F642  |
    |   |
        |
        |
        =========''', '''
    Concentrate, my life is in your hands!

    +---+
    |   |
    \U0001F972   |
   /|   |
        |
        |
        =========''', '''
    Uhmm...

    +---+
    |   |
    \U0001F614  |
   /|\\  |
        |
        |
        =========''', '''
    Come on my friend!

    +---+
    |   |
    \U0001F627  |
   /|\\  |
    |   |
        |
        =========''', '''
    You can do it!

    +---+
    |   |
    \U0001F625  |
   /|\\  |
    |   |
   /    |
        =========''', '''
    Help help!

    +---+
    |   |
    \U0001F630  |
   /|\\  |
    |   |
   / \\  |
        =========''', '''
    I'm alive. Thanks guy!

    
    
        \U0001F973
       \|/
        | 
       / \\
    =========''', '''
    Dead!

    +---+
    |   |
    \U0001F635  |
   /|\\  |
    |   |
   / \\  |
=\     /=========''']


def enter_letter():
    ''' Validate the letter entered by user is valid '''

    while True:
        try:
            letter = input('\nEnter a letter: ')
            if len(letter) > 1 or not letter.isalpha():
                raise ValueError
            return letter
        except ValueError:
            print('You only  have to enter one letter')


def read_data():
    ''' Read words list from file '''

    words = []
    try:
        with open('data.txt', 'r', encoding='utf-8') as f:
            words = [line.strip('\n') for line in f]
    except FileNotFoundError:
        print('Validate both path and file name are correct')

    return words


def draw_word(word, tries):
    ''' Shows the hanged man with the hidden word '''

    os.system('clear')
    print('''***** Hangman Game *****''')
    print(IMAGES[tries])
    for letter in word.values():
        for k, v in letter.items():
            print(v.upper(), end=' ')
    print()


def validate_letter(word, letter):
    ''' Check if the letter entered is correct or not
    and update the hidden word with the letter if
    its correct'''

    valid = False
    for k, v in word.items():
        if v.get(letter.lower()):
            v[letter] = letter
            valid = True

    return word, valid


def run():
    ''' Main fucntion for Hangman Game '''

    tries = 0
    correct_letter = False
    hidden_word = {}
    try:
        words = read_data()
        if len(words) == 0:
            raise Exception

        word = random.choice(words)

        hidden_word = {
            i: {unidecode(value): '_'}
            for i, value in enumerate(word)
        }
    except Exception:
        print('There is no words to choose and play :(')
        return

    while tries < 8:
        draw_word(hidden_word, tries)
        letter_entered = enter_letter()
        hidden_word, correct_letter = validate_letter(
            hidden_word, letter_entered
        )

        if not correct_letter:
            tries += 1

        if not any('_' in v.values() for v in hidden_word.values()):
            break

    if not any('_' in v.values() for v in hidden_word.values()):
        draw_word(hidden_word, 8)
        print(f'You won the game \N{nerd face}!')
    else:
        draw_word(hidden_word, 9)
        print(f'You lose the game \N{smiling face with tear} The word was {word}')


if __name__ == '__main__':
    run()
