from random import sample
characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+'
choice = int(input('Enter how you want tour password to be(1 for easy,2 for medium,3 for difficult) : '))
strength = {1: 3, 2: 6, 3: 8}
password_length = strength[choice]
password = sample(characters, password_length)
password = "".join(password)
print('Suggested password for you is:', password)

