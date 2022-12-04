import random

# get the random number to guess
def get_random_number(x):
    return random.randint(0, x)

# check the number and print a clue for the guesser
def comparaisson(random_number, guess):
    if guess < random_number:
        print('Sorry, your number is too low.')
    elif guess > random_number:
        print('Sorry, your number is too high')
    else:
        print('Congrats! You get it.')

# start the game
def guess(x):
    random_number = get_random_number(x)
    guess = -1
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        comparaisson(random_number, guess)

# get the rules from the user    
range = int(input('Tell me the highest number of the range you want to play with: '))
print (f'Ok! You have to guess from 1 to {range}')
guess(range)