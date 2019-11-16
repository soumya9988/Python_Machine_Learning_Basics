student_grades = {'Mary': 8.8,
                  'John': 7.5,
                  'Kia': 6.1}

# Accessing the elements
print('The students in the class are: ')
for student in student_grades:
    print(student)

sum_of_marks = sum(student_grades.values())
no_of_students = len(student_grades)
avg_marks = sum_of_marks/ no_of_students
print('Avg of marks of the students in the class is:', avg_marks)

# index of dictionary
print(student_grades['Mary'])