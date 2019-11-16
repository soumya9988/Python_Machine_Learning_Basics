def max_num(a, b):
    if a > b:
        return a
    else:
        return b


def min_num(a, b):
    if a < b:
        return a
    else:
        return b


number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))
if number1 != number2:
    max_no = max_num(number1, number2)
    print('%d is the greater number' % (max_no))
    min_no = min_num(number1, number2)
    print('%d is the smaller number' % (min_no))
else:
    print('Both are equal')
