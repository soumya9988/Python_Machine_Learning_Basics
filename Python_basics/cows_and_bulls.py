from random import randint


gen_num = str(randint(1000, 9999))
while True:
    cow_bull = [0, 0]
    user_choice = input('Enter the number: ')
    for i in range(len(gen_num)):
        if user_choice == gen_num:
            cow_bull = [4, 0]
            print('Bingo...')
            break
        elif gen_num[i] == user_choice[i]:
            cow_bull[0] += 1
        elif gen_num[i] in user_choice:
            cow_bull[1] += 1
    print('You have %s cows and %s bulls' % (cow_bull[0], cow_bull[1]))
    if cow_bull[0] != 4:
        choice_quit = input('Type exit to quit.. Else type yes...')
        if choice_quit == 'exit':
            break
    else:
        break




