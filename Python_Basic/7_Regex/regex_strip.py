import re


def regex_strip(string, char=' '):
    """
    (str, char) --> str
    Takes a string and does the same thing as the strip() string method.
    If no char is passed with string, then whitespace characters will be removed from the beginning and end of string.
    Otherwise, the char specified  will be removed from the string.
    >>> regex_strip('This is a monkey', 'is')
    Th  a monkey
    >>> regex_strip('        Hello World       ')
    Hello World
    """
    if char == ' ':
        char_format = re.compile(r'^\s*|\s*$')
        check_format = char_format.sub('', string)
        return check_format
    else:
        char_format = re.compile(char)
        check_format = char_format.sub('', string)
        return check_format


print(regex_strip('This is a monkey', 'is'))
print(regex_strip('Agent XXXX is now following XXXX in Malibu', 'X'))
print(regex_strip('        Hello World       '), 'Hi')
print(regex_strip('        Hello      World'), 'Hi')
print(regex_strip('Hello     World      '), 'Hi')
