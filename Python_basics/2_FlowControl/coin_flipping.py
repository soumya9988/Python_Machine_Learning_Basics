from random import randint
times = int(input('Please enter the number of times you want to flip the coin: '))
result = ""
heads = 0
tails = 0


while times > 0:
    times -= 1
    coin = randint(1,2)
    if coin == 1:
        heads += 1
        result += 'H'
    else:
        tails += 1
        result += 'T'


print('The result after flipping the coin is:', result)
print('Heads : %d, Tails : %d' % (heads, tails))

