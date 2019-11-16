student_grades = [9.7, 10, 5, 3, 7.5, 2, 10, 6, 10]

# Adding an element to the list
student_grades.append(13.5)
print(student_grades)

# getting the index of the element
ind = student_grades.index(7.5)
print('The index is:', ind)
elem = student_grades.__getitem__(5)
print('The sixth element in the list is:', elem)

# list slicing
country = ['Mosambique', 'India', 'UK', 'Germany', 'Mexico', 'Portugal']
slices = country[-5:-1:2]
print('Sliced version of country is:', slices)
country_slice = country[0][1:4]
print('Slices of the first country is:', country_slice)


student_grades.remove(10)
print(student_grades)

del_item = student_grades.pop(1)
print(student_grades, del_item)
