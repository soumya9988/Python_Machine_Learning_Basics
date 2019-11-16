number = 25
guess = int(input("Enter your guess: "))
if number == guess:
    print('Correctly guessed')
elif number < guess:
    print(' Your guess is higher than number')
else:
    print('Your guess is lower than number')
print('Out of guess logic for if!')


while True:
    guess = int(input('Enter your guess:'))

    if guess < 10:
        print('Guessed value is too small!!')
        continue
    if guess < number:
        print('Guess is less than number')
    elif guess == number:
        print('Correct guess')
        break
    else:
        print('Guess is greater than number')

print('Out of guess block for while')


for i in range(0,10):
    print(i)
