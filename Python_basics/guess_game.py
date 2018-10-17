from random import randint
from time import sleep

while True:
    choice = int(input('Please enter a number: '))
    comp_choice = randint(1, 100)
    print('Generating computer choice...')
    sleep(1)
    print('Computer choice is', comp_choice)
    if choice == comp_choice:
        print('You guessed it right!!')
    elif choice > comp_choice:
        print('Your guess is too high!!')
    else:
        print('Your guess is too low!!')
    cont = input('Do you wanna keep guessing.. Type exit to quit! ')

    if cont.lower() == 'exit':
        break


