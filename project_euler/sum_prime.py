def is_prime(number):
    if number == 2:
        return True
    else:
        for i in range(2, number-1):
            if number % i == 0:
                return False
        return True

sum_of_prime = 0
for i in range(2, 2000000):
    if is_prime(i):
        sum_of_prime += i
print(sum_of_prime)

