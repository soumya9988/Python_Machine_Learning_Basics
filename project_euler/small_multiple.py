def is_divisible(number):
    is_divisible = True
    for i in range(1,21):
        if number % i != 0:
            is_divisible = False
            return is_divisible
    return is_divisible


number = 1
while True:
    if is_divisible(number):
        print(number)
        break
    else:
        number = number + 1




