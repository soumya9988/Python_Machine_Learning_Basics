from datetime import datetime
from random import randint

# Character input
name = input('Please enter your name:')
age = int(input('Please enter your age: '))
year = 100 - age + int(datetime.now().strftime('%Y'))
print('Hi %s, You will be 100 years old in %d..' % (name, year))


# List and conditional
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
number = int(input('Enter a number: '))
for item in a:
    if item < number:
        new_list.append(item)

print(new_list)

# Divisor
div_list = []
div_num = int(input('Please enter the number whose divisor is to be printed: '))
for i in range(2, div_num+1):

    if div_num % i == 0:
        div_list.append(i)

print('The divisors of the number are: ', div_list)

# List overlap
list1 = [x for x in range(1, randint(1, 25))]
list2 = [1, 1, 3, 5, 5, 12, 45, 23, 17, 12, 23, 1, 3, 5]
new_combined_list = []
print('First list: ', list1)
print('Second list: ', list2)
for item in list1:
    if item in list2 and item not in new_combined_list:
        new_combined_list.append(item)
new_combined_list.sort()
print('The new combined list is:', new_combined_list)

# String slicing
check_str = input('Enter a string: ')
if check_str.lower().replace(" ", "") == check_str[::-1].lower().replace(" ", ""):
    print('Above string is a Palindrome')
else:
    print('The above string is not a palindrome')

# List comprehension
list_comp = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
new_list = [item for item in list_comp if item % 2 == 0 ]
print(new_list)
end_list = [list_comp[0], list_comp[(len(list_comp) - 1)]]
print(end_list)


# String splitting and reversing.
new_set = []
words = input('Please enter a sentence: ')
new_set = words.split(" ")
reverse_set = []
for item in new_set:
    reverse = item[::-1]
    reverse_set.append(reverse)
mod_text = " ".join(reverse_set)
print('The modified sentence is: ')
print(mod_text)














