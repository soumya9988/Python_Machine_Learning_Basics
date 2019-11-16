phone_numbers = {"John Smith": "+37682929928",
                 "Marry Simpons": "+423998200919",
                 "David Attenborogh":"+17156789923",
                 "Lily Joe": "+919448785643"}
print('Numbers:')
for number in phone_numbers.values():
    print(number.replace('+', '00'))

print('Contacts:')
for item in phone_numbers.items():
    print(item)

print('Names: ')
for name in phone_numbers.keys():
    print(name)

print('Default:')
for key, value  in phone_numbers.items():
    print(key,': ', value)

