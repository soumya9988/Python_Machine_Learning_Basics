def is_prime(n):
    if n == 2:
        return True
    else:
        for i in range(2, n - 1):
            if n % i == 0:
                return False
        return True


def get_prime(number):
    new_number = number + 1
    while True:
        check = is_prime(new_number)
        if not check:
            new_number += 1
        else:
            return new_number


number = int(input('Enter the number:'))
running = True
while running:
    number = get_prime(number)
    print('The next prime number is ', number)
    choice = input('Do you want to find next prime number? Type quit to exit...')
    if choice.lower() == 'quit':
        break
    else:
        number += 1



