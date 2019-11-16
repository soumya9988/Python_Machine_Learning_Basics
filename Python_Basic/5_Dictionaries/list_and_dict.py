from time import sleep
from random import randint

running = True
choices = ['ROCK', 'PAPER', 'SCISSORS']
messages = {0: "Yeyyy, you won", 1: "Ohoo that's a tie", 2: "Aww you lost"}


def get_comp_choice():
    choice = int(randint(0, 2))
    com_choice = choices[choice]
    return com_choice


def decide_winner(user, comp):
    if user == comp:
        print(messages[1])
    elif (user == choices[0] and comp == choices[2]) or (user == choices[1] and comp == choices[0]) or (user == choices[2] and comp == choices[1] ):
        print(messages[0])
    else:
        print(messages[2])

while running:
    user_choice = input('Enter your choice; ROCK, PAPER or SCISSORS: ')
    user_choice = user_choice.upper()
    sleep(1)
    comp_choice = get_comp_choice()
    print('Computer choice is %s' % (comp_choice))
    decide_winner(user_choice, comp_choice)
    sleep(1)
    cont = input('Do you want to continue? Type quit to exit..')
    cont = cont.upper()
    if cont == 'QUIT':
        running = False


