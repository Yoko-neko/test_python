# It doesn't seem to load the words in the list. I can't play games.

import random
import time


print('Welcome to hangman game!')
name = input('Enter your name: ')
print('Hello {}! Best of luck!'.format(name))
time.sleep(1)
print('The game is about to start!')
time.sleep(2)

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    word = random.choice(['apple','orange','banana','red','blue','green','pink','Yellow'])
    length = len(word)
    count = 0
    display = '_'*length
    already_guessed = []
    play_game =""

def play_loop():
    global play_game
    play_game = input('Do you want to play again? y = yes, n = no : ')
    while play_game not in ['y','n','Y','N']:
        play_game = input('Do you want to play again? y = yes, n = no : ')
    if play_game == 'y':
        main()

    elif play_game == 'n':
        print('Thank you for playing! We expect you back again!')
        exit()

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input('This is the Hangman word:{} Enter your guess: '.format(display))
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip())>=2 or guess<='9':
        print('Invalid input,Try a letter')
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + guess + display[index + 1:]
        print(display+'\n')

    elif guess in already_guessed:
        print('Try another letter.')

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print('     \n'
                  '|   \n'
                  '|   \n'
                  '|   \n'
                  '|   \n'
                  '|   \n'
                  '|   \n'
                  ' |  \n')
            print('Wrong guess.'+ str(limit-count)+ 'guesses remaining ' )

        elif count == 2:
            time.sleep(1)
            print('     \n'
                  '|  |\n'
                  '|  |\n'
                  '|   \n'
                  '|   \n'
                  '|   \n'
                  '|   \n'
                  ' |  \n')
            print('Wrong guess.'+ str(limit-count)+ 'guesses remaining ' )

        elif count == 3:
            time.sleep(1)
            print('     \n'
                  '|  |\n'
                  '|  |\n'
                  '|  |\n'
                  '|   \n'
                  '|   \n'
                  '|   \n'
                  ' |  \n')
            print('Wrong guess.'+ str(limit-count)+ 'guesses remaining ' )

        elif count == 4:
            time.sleep(1)
            print('     \n'
                  '|  |\n'
                  '|  |\n'
                  '|  |\n'
                  '|  O\n'
                  '|   \n'
                  '|   \n'
                  ' |  \n')
            print('Wrong guess.'+ str(limit-count)+ 'last guess remaining ' )

        elif count == 5:
            time.sleep(1)
            print('     \n'
                  '|  |\n'
                  '|  |\n'
                  '|  |\n'
                  '|  O\n'
                  '| /|\n'
                  '| / \n'
                  ' |  \n')
            print('Wrong guess.You are hanged!!!' )
            print('The word was' + already_guessed.word)
            play_loop()

    if word == '_'*length:
        print('Congrats!You have guessed the word correctly!')
        play_loop()

    elif count != limit:
        hangman()

main()
hangman()