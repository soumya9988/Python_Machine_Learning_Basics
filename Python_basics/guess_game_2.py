from random import randint
from time import sleep
user_input = int(input('Enter your guess: '))
no_of_guess = 0
min_limit = 0
max_limit = 100

while True:
    computer_choice = randint(min_limit, max_limit)
    print('Computer choice is', computer_choice)
    sleep(1)

    no_of_guess += 1
    if user_input == computer_choice:
        print("Bingo!! You guessed it right in %d chances.." % no_of_guess)
        break
    elif user_input > computer_choice:
        min_limit = computer_choice
    else:
        max_limit = computer_choice
    if min_limit >= max_limit:
        break

