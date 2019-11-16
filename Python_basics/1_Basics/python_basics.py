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


def sort_alpha_num(s):
    i = s.split(None, 1)[0]
    if i.isnumeric():
        return int(i)
    return s


def main():
    print_arg()
    repeat_exclaim('Hello ', True)
    line = input('Enter the sentence separated by space: ')
    list_words = line.split(' ')
    set_word = set(list_words)
    set_word = sorted(set_word, key=sort_alpha_num, reverse=True)
    print(', '.join(set_word))
    sys.exit(0)


if __name__ == '__main__':
    main()





