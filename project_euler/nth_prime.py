def is_prime(number):
    if number == 2:
        return True
    else:
        for i in range(2, number-1):
            if number % i == 0:
                return False
        return True

i = 2
count = 0
prime_list = []
while count < 10001:
    if is_prime(i):
        count += 1
        prime_list.append(i)

    i += 1

print(prime_list)
