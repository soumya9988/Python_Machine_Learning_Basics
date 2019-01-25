'''
Project: Renaming Files with American-Style Dates(ASD) to European-Style Dates
It searches all the filenames in the current working directory for American-style dates.
When one is found, it renames the file with the month and day swapped to make it European-style.
Eg: This will check for ASD as in 12-11-1980 and 09-08-1989. But it should not read
    12.12.1990 , 13-01-1998 , 01-32-2015 , 01-01-123 and 12345667. But these are very valid dates:
    01-1-2019."
'''


import re
import os
import shutil


# American style date pattern
regex_american_date =  re.compile(r"""(^(.*?)
                                       (([0][0-9])|(1[0-2]))
                                       (/|\.|-)
                                       (([0][1-9])|([1-2][0-9])|(3[0|1]))
                                       (/|\.|-)
                                       (\d{2}|\d{4})
                                       (.*?)$
                                       )""", re.VERBOSE)

# Getting all the text files in the current working directory
path_cwd = os.getcwd()
text_files = [files for files in os.listdir(os.getcwd()) if files.endswith('.txt')]

for file_name in text_files:
    asd_pattern = regex_american_date.search(file_name)
    if asd_pattern:
        print(asd_pattern.group())
        # Extracting the date from file name for conversion
        before_part = asd_pattern.group(2)
        asd_month = asd_pattern.group(3)
        separator = asd_pattern.group(6)
        asd_day = asd_pattern.group(7)
        asd_year = asd_pattern.group(12)
        after_part = asd_pattern.group(13)

        # European date pattern: DD-MM-YYYY
        esd_pattern = before_part + asd_day + separator + asd_month + separator + asd_year+ after_part

        # Renaming the file from ASD to ESD
        source_file = os.path.join(path_cwd, file_name)
        dest_file = os.path.join(path_cwd, esd_pattern)
        print('Renaming %s to %s' % (source_file, dest_file))
        shutil.move(source_file, dest_file)



