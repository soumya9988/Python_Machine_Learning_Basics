from random import randint
from time import sleep


def roll_dice():
    first_dice = randint(1, 6)
    second_dice = randint(1, 6)
    total_val = first_dice + second_dice
    return total_val


def print_outcome(guess, tot):
    if guess == tot:
        print('You won!!!')
    else:
        print('Sorry! Wrong guess...')


guess_tot = int(input('Enter your guess for total value of dice!'))
print('Rolling.....')
random_tot = roll_dice()
sleep(5)
print_outcome(guess_tot, random_tot)
