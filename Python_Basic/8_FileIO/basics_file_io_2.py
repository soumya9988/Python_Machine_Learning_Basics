full_path = '/Users/vedhoos/hobby_python_proj/Python_basics/alice.txt'
name_path = '/Users/vedhoos/hobby_python_proj/Python_basics/name_list.txt'


with open(full_path, 'r') as alice_file:
    content = alice_file.read()
print(content)
print(alice_file.closed)

with open(name_path, 'r') as name_file:
    name_with_L = []
    name_list = name_file.readlines()
for name in name_list:
    if name[0] == 'L':
        name_with_L.append(name.strip())
unique_names = set(name_with_L)
print(unique_names)

names_to_write = str(name_with_L)
with open('names_file.txt', 'w') as file_to_write:
    file_to_write.write(names_to_write)

with open('names_file.txt', 'a') as file_to_write:
    file_to_write.write('\n Names appended after this:\n')
    file_to_write.write(names_to_write)



