# The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
# The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.

tries = 10

print('\nWelcome to the hangman game.')
print('Here are the rules:')
print('1. A secret word has been chosen.\n2. You have',tries,'tries to guess the word.\n3. Each incorrect guess brings you closer to being \"hanged\".')

def fun(i):
    count = int(tries)
    letter = []
    word = []
    for j in list(i):
        word.append('_')
    while True:
        if word == list(i):
            print('\nCONGRATULATION!!!, you guessed the word ', '\'',*word, '\'', sep='')
            break
        print('\nYou have',count,'tries left')
        print('Used letters:', *letter, sep = ' ')
        print('Word:',*word, sep = ' ')
        letter_1 = input('Guess a letter: ')
        if letter_1 not in letter:
            letter.append(letter_1)
        word_1 = list(i)
        for e in range(len(word_1)):
            if letter_1 == word_1[e]:
                word[e] = letter_1
            else:
                continue
        if letter_1 not in i:
            count -= 1
        else:
            continue
        if count == 0:
            print('\nGame over, YOU LOSE')
            break
        else:
            continue

gameword = 'let'
fun(gameword)