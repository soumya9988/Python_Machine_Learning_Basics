import random

low = 1
high = 50
no_of_guess = 0
random_no = random.randint(low, high)
print('I am thinking of a number between 1 and 50.')

while True:
    no_of_guess += 1
    guess = int(input('Take a guess. '))
    if guess == random_no:
        print('Good job! You guessed my number in %d guesses!' % no_of_guess)
        break
    elif guess > random_no:
        print('Your guess is too high.')
    else:
        print('Your guess is too low.')
