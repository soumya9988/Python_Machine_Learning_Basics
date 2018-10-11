def fibonacci():
    series = [1]
    lim = int(input('Enter the no of fibonacci number that you want to print: '))
    print('First %d numbers of Fibonacci series are: ' % lim)
    while len(series) < lim:
        if len(series) == 1:
            series.append(1)
        else:
            series.append(series[-1] + series[-2])

    print(series)


def factorial(n):
    if n == 0:
        return 1;
    else:
        return n * factorial(n - 1)


while True:
    choice = int(input('Enter 1 to get Fibo series, 2 to find factorial of the number, 3 to exit: '))
    if choice == 1:
        fibonacci()
    elif choice == 2:
        n = int(input('Enter the number whose factorial is to be found: '))
        fact = factorial(n)
        print('Factorial of %d is %d' % (n, fact))
    else:
        print('Quitting...')
        break
