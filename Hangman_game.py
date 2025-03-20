# Hangman Game in Python


import random

word='Apple Banana Mango Orange Pineapple Grapes Watermelon Strawberry Papaya Pomegranate'

spl_word=word.split(' ')
sel_rand_word=random.choice(spl_word).upper()
print(sel_rand_word)
chances=len(sel_rand_word)+2
guesses_word=''
for _ in sel_rand_word:
    print(' _ ',end='')

while chances!=0:

    
    if len(guesses_word)!=len(sel_rand_word):
        try:
            char_guess=str(input('\n Enter a letter to guess: ')).upper()
        except :
            print('Enter only a letter!: ')
            continue
        if not char_guess.isalpha():
                print('Enter only a LETTER')
                continue
        elif len(char_guess) > 1:
                print('Enter only a SINGLE letter')
                continue
        elif char_guess in guesses_word:
                print('You have already guessed that letter')
                continue
        chances-=1
        # print(char_guess)
        for i in sel_rand_word:
            if char_guess == i:
                guesses_word+=char_guess
                
        
        for j in sel_rand_word:
            if j in guesses_word:
                print( j ,end=' ')
            else:
                print(' _ ',end=' ')
    else:
        break
if chances !=0:
    print("\n The word is: ", end=' ')
    print(sel_rand_word)           
    print('\n Congratulations, You won!')
else:
    print()
    print('\n You lost! Try again..')
    print('\n The word was {}'.format(sel_rand_word))