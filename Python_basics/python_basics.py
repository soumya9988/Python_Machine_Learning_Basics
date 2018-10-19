import sys


def print_arg():
    print(sys.argv)


def repeat_exclaim(word, exclaim):
    print_str = 'Hello'
    print_str += 'there'
    print(print_str)
    for letter in print_str:
        print(letter, end=',')
    print((word * 3), end='')
    if exclaim:
        print('!!!')
    print('-' * 20)


def main():
    print_arg()
    repeat_exclaim('Hello ', True)
    sys.exit(0)


if __name__ == '__main__':
    main()


