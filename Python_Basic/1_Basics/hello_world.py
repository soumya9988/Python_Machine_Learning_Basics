print('Hello World!!')

# Introducing print,input, type casting and len()
my_name = input('Enter your name.. ')
print('It\'s good to meet you', my_name)
print('The length of your name is', len(my_name))
my_age = int(input('Please enter your age: '))
print('You will be %d years old in a year' % ( my_age + 1 ))

# Keyword arguments
print('cats', 'dogs', 'bulls', sep='* ')

# Below steps calculate the value of pi and round it to two decimal places
pi = 22 / 7
print(round(pi, 2))