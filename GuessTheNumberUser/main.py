import random

# start the game
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        # prepare next guess
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        # get feedback from user
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()
        # prepare the next guess
        if feedback == 'h' and guess > low:
            high = guess - 1
        elif feedback == 'l' and guess < high:
            low = guess + 1
        elif feedback == 'c':
            print(f'Congrats! I get it. The number was {guess}.')
        else:
            print('Wrong feedback. Please try again')


# get the rules from the user    
range = int(input('Tell me the highest number of the range you want to play with: '))
print (f'Ok! I have to guess from 1 to {range}')
computer_guess(range)