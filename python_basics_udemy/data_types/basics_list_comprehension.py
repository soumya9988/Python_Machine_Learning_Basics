# List comprehension with if condition
temps_in_degrees = [23, 34, 17, 6, 13.5, -9999]
temp_in_kelvin = [(temp + 273.15) for temp in temps_in_degrees if temp != -9999]
print(temp_in_kelvin)

# List comprehension with if- else condition
converted_temp = [(temp + 273.15) if temp != -9999 else 0 for temp in temps_in_degrees]
print(converted_temp)

foo = [99, 'no data', 95, 94, 'no data']
integer_foo = [foo_elem if type(foo_elem) == int else 0 for foo_elem in foo ]
print(integer_foo)
sum_foo = sum([foo_elem if type(foo_elem) == int else 0 for foo_elem in foo ])
print(sum_foo)
