number_range = list(range(1, 100, 7))
print(number_range)

# To get the details of data types
print(dir(str))

# Inbuilt functions of list
student_grades = [9.7, 10, 5, 3, 7.5, 2, 10, 6, 10]

sum_of_grades = sum(student_grades)
print('Sum of the grades for the student is: ', sum_of_grades)

no_of_subjects = len(student_grades)
print('No of subjects is: ', no_of_subjects)

avg_mark = sum_of_grades/ no_of_subjects
print('Average mark for the student is: ', avg_mark)

best_score = student_grades.count(10)
print('Student got a perfect score', best_score, 'times' )

# split and join
long_text = 'I have miles to go before i sleep, miles to go before i sleep'
split_text = long_text.split(',')
print(split_text)
rejoined_text = '...'.join(split_text)
print(rejoined_text)

spam = ['apples', '129' , 'broccoli', 'bananas', '3.14', 'cats', 'dogs', 'pigeons']
string_spam = ', '.join(spam) + '.'
print(string_spam)

sentence = '    My name is Catherine     . I love to have some icecream.      '
list_words = sentence.split()
print(list_words)

# looping through the elements:
for grade in student_grades:
    print(grade)



