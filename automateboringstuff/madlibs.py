"""
Chapter 8 – Reading and Writing Files

Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word
ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

"""
import re
# Reading the contentc of the madlibs text file present in the folder
file_path = '/Users/vedhoos/hobby_python_proj/automateboringstuff/madlibs_text.txt'
with open( file_path, 'r') as text_file:
    text = text_file.read()

# Check for noun/verb/adverb/adjective in the text read above and replace with user input
regex = re.compile((r'ADJECTIVE|NOUN|VERB|ADVERB'))
for word in regex.findall(text):
    replacement = input('Enter the replacement for %s: ' % word)
    text = regex.sub(replacement, text, 1)

# Finally writing the contents after replacing with user input into another file
with open('madlibs_replacement.txt', 'w') as output_file:
    output_file.write(text)




