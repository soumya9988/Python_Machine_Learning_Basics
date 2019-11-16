birth_calender =  {'Anna Franklin': '21.Mar.1990',
                   'Lisa Thompson': '11.Feb.1990',
                   'Sally Carera' : '09.Aug.1990',
                   'Bernard Most' : '31.Jan.1990',
                   'Charles Fuge' : '25.Nov.1990',
                   'George Louise': '17.May.1990',
                   'Charlotte Mary': '06.Jun.1990',
                   'Jack Thomas' :  '27.Dec.1990',
                   'Elza McDormick': '12.Oct.1990'}
print('*****Welcome to the birthday dictionary. We know the birthdays of****')
for keys in birth_calender:
    print(keys)

choice = input('Who\'s birthday do you want to look up? ')
if choice in birth_calender:
    birthday = birth_calender[choice]
    print('%s\'s birthday is on %s' % (choice, birthday))
else:
    print('Sorry...We don\'t know the birthday!!')

