import os
work_dir = os.getcwd()

# Reading the contents with readlines
file_name = os.path.join(work_dir, 'fruits.txt')
with open(file_name) as f_name:
    content = f_name.readlines()
print(content)

# Reading the entire file in one go using read
with open(file_name) as f_name:
    content = f_name.read()
    print(content)

# Reading one line at a time.
with open(file_name, errors='ignore') as f_name:
    content = f_name.readline()
    while content:
        print(content.strip())
        content = f_name.readline()

bear_file = os.path.join(work_dir, 'bear.txt')
with open(bear_file, 'r', errors='ignore') as new_file:
    bear_text = new_file.read()
if bear_text:
    bear_txt_trim = bear_text[:90]
    print(bear_txt_trim)

# Writing to a file
file_orig = os.path.join(work_dir, 'Maya_Angelou.txt')
file_copy = os.path.join(work_dir, 'Caged_Bird.txt')
with open(file_orig, 'r') as f_orig:
    content = f_orig.read()
    if content:
        with open(file_copy, 'w') as f_copy:
            f_copy.write(content)

# Appending to a file
author = '     -Maya Angelou'
with open(file_copy, 'a') as auth:
    auth.write(author)
