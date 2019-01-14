def check_palindrome(number):
    return str(number)[0:] == str(number)[-1::-1]


if __name__ == '__main__':
    i = 100
    new_max = 0
    while i < 999:
        j = 100
        while j < 999:
            prod = i * j
            if check_palindrome(prod):
                new_max = max(prod, new_max)
            j = j + 1
        i = i + 1

    print(new_max)




