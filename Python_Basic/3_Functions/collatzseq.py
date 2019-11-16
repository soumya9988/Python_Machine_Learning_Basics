def collatz(number):
    """
    (int) -> int
    If number is even, then print number // 2 and return this value.
    If number is odd, then  print and return 3 * number + 1.
    >>> collatz(3)
    10
    >>> collatz(10)
    5
    """
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
    print(number)
    return number


try:
    number = int(input('Enter the number: '))
    while number > 1:
        number = collatz(number)
except ValueError:
    print('Please enter an integer value!!')
