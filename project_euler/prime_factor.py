def prime_factors(number):
    factor_list = []
    i = 2
    while i <= number:
        if number % i == 0:
            factor_list.append(i)
            number /= i
        else:
            i = i + 1
    return factor_list

print(max(prime_factors(600851475143)))