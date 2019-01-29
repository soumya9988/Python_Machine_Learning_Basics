'''To remove the zeros from files such as spam0042.txt'''

import os
import re
import shutil
from time import sleep

# Creating a text file for testing purpose"
path_cwd = os.getcwd()
sample_text_file = os.path.join(path_cwd, 'spamfile_002.txt')
with open( sample_text_file, 'w') as new_file:
    new_file.write('This is for testing')
sleep(3)

# Regex expression to check for 0 in file
spam_file_re = re.compile(r'[0]*')
text_files = [files for files in os.listdir(path_cwd) if files.endswith('.txt') and
                                                        files.startswith('spam')]

# finally renaming the file by removing the zeroes in the filename
for file in text_files:
    file_name = spam_file_re.sub('', file)
    if file != file_name:
        source_file_name = os.path.join(path_cwd, file)
        dest_file_name = os.path.join(path_cwd, file_name)
        print('Renaming %s to %s...' % (source_file_name, dest_file_name))
        shutil.move(file, dest_file_name)


