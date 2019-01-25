"""
Chapter 8 – Reading and Writing Files

Write a program that opens all .txt files in a folder and searches for any line that
matches a user-supplied regular expression. The results should be printed to the screen.

"""
import os
import re
search_result = []

# To get all the text files in the current working directory
cur_dir = os.getcwd()
all_files = os.listdir(cur_dir)
text_files = [file_name for file_name in all_files if file_name.endswith('.txt')]

# Get the pattern to search from the user
print('\nThis program searches for lines in text file that matches the string pattern you enters.')
string_to_search = input('Please enter the string to search: ')

# Regex to match the sentence with the string obtained from user
regex = re.compile(r'.*(%s).*' % string_to_search)

# Check for the string pattern in all the text files in the folder.
for file in text_files:
    with open(file, 'r') as input_file:
        content = input_file.read()
        for match in regex.finditer(content):
            search_result.append(match.group())

# Finally printing the output in the screen
if search_result:
    print('\nThe search is successful with following results:')
    for lines in search_result:
        print(lines)
else:
    print('Sorry, no such pattern found!!')

