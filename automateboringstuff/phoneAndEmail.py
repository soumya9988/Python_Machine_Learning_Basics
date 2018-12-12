import re, pyperclip

matches = []
unique_phone_num = set()
email_list = []
unique_email_id =set()

"""
    Creating a regex format for phone number.
    Eg format for telephone in US: (541) 754-3010 or 754-3010
    ie. Optional area code and separator, followed by first 3 digits, separtor and last 4 digits
"""
phone_regex = re.compile(r'(\d{3}|\(\d{3}\))?(\s|\-|\.)?(\d{3})(\s|\-|\.)(\d{4})')

"""
    Creating a regex format for email id.
    Eg format for email id : abc@yahoo.com, popeyethesailor12@dumbo.in
"""
email_regex = re.compile(r'\w+@[A-Z0-9]+\.[a-z]{2,4}', re.IGNORECASE)

# Get the text copied in the clipboard into text variable.
text = str(pyperclip.paste())

# Find all unique phone numbers and email addresses in the text.
for groups in phone_regex.findall(text):
    phone_num = ''
    for index in groups:
        phone_num += index
    matches.append(phone_num.strip())
    unique_phone_num = set(matches)

email_list = email_regex.findall(text)
unique_email_id = set(email_list)

# Printing the email id and phone number
if len(unique_phone_num) > 0 or len(unique_email_id) > 0:
    print('Phone numbers and email ids in the text are: ')
    for number in unique_phone_num:
        print(number)
    for mail_id in unique_email_id:
        print(mail_id)
else:
    print('No phone numbers or email addresses found.')


