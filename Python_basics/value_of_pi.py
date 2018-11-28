def calc_pi(iter):
    """
    (int) --> float
    Function that calculate the value of Pi using Leibniz formula and returns the value of pi.
    pi/ 4 = 1 - 1/3 + 1/5 - 1/7 + 1/9... where iter is the number of times the sequence repeats.

    """
    sum = 0
    num = 1
    den = 1
    for i in range(iter):
        sum = sum + ( num / den)
        num *= -1
        den += 2
    return sum * 4

print(calc_pi(200000))