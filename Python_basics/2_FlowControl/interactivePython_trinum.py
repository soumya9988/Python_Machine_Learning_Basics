choice = True


def get_triangular_value(n):
    return (n * (n +1))/2


while choice:
    value = int(input('Enter the number of triagular value you have to find:'))
    for i in range(1, value + 1):
        print(i,'\t',int(get_triangular_value(i)))
    choice = input('Press any key to continue. Press enter to quit...')
