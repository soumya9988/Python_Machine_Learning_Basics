import re


def has_vowels(str):
    pattern = re.compile(r'[aeiou]', re.IGNORECASE)
    check = pattern.search(str)
    return bool(check)


def is_integer(str):
    pattern = re.compile(r'^-*[0-9]+')
    check = pattern.search(str)
    return bool(check)


def is_fraction(str):
    pattern = re.compile(r'^-*[0-9]+/[0-9]+')
    check = pattern.search(str)
    den = str.split('/')
    if len(den) > 1:
        if den[1] == '0':
            return False
    return bool(check)


def get_file_extension(str):
    pattern = re.search(r'(.\w+$)', str)
    return pattern.group()


def hexadecimal(str):
    pattern = re.compile(r'\b[a-f]+\b', re.IGNORECASE)
    check = pattern.findall(str)
    return check

print('Vowels in Monday:' , has_vowels('Monday is a holiday'))
print('Vowels in Fly:', has_vowels('Fly spy dry sky'))
print(is_integer(""))
print(is_integer(" 5"))
print(is_integer("5000"))
print(is_integer("-999"))
print(is_integer("+999"))
print(is_integer("00"))
print(is_integer("0.0"))
print(is_integer("99.1"))
print(is_fraction(""))
print(is_fraction("5000"))
print(is_fraction("-999/1"))
print(is_fraction("+999/1"))
print(is_fraction("00/1"))
print(is_fraction("5/010"))
print(is_fraction("5/0"))
print(is_fraction("/5"))
print(get_file_extension('archive.tar.gz'))
print(get_file_extension('index.xhtml'))
print(hexadecimal('This is decaf coffee for bead and bread in cafe'))