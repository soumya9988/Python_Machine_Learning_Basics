from PIL import Image
import pytesseract
import os
import re

# Setting the regex email ID pattern
pattern = re.compile(r'\w+@[A-Z0-9]+\.[a-z]{2,4}', re.IGNORECASE)

# Getting all the jpg files in the current working directory
cwd_path = os.getcwd()
jpg_files = [files for files in os.listdir(cwd_path) if files.endswith('.jpg')]

# Looping through the jpg files
for jpg_file in jpg_files:
    file_name = os.path.join(cwd_path, jpg_file)

    # Reading the text in the jpg files
    text = pytesseract.image_to_string(Image.open(file_name))

    # Extracting the email IDs and printing it
    for email_id in pattern.findall(text):
        print('Email ID in %s are %s' % (file_name, email_id))



