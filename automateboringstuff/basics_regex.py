import re


def check_phone_no(phone_number):
    """
    (string) --> bool
    A function which accepts the string 'phone number' and checks if it is a valid format and return the
    result as a boolean
    >>> print(check_phone_no('415-555-4242'))
    True
    >>> print(check_phone_no('Abc-123-1234'))
    False
    """
    match_phone_no = re.compile(r'\d{3}-\d{3}-\d{4}')
    #group_phone_no = match_phone_no.search(phone_number)
    #if group_phone_no:
        #return group_phone_no.group()
    return bool(match_phone_no.search(phone_number))


def find_all_phone_no(message):
    """
    (string) --> list[phone nos]
    A function that accepts a message and return a list of phone numbers extracted from the message
    >>> find_all_phone_no('Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.')
    ['415-555-1011', '415-555-9999']
    >>> find_all_phone_no('Meet me at 1402-566 Arlington Avenue or call me at 814-098-7522')
    ['814-098-7522']
    """
    match_phone_no = re.compile(r'\d{3}-\d{3}-\d{4}')
    list_phone_no = match_phone_no.findall(message)
    return list_phone_no


def optional_words(message):
    match_bat = re.compile(r'Bat(man|cave|bike|coptor)')
    group_bat = match_bat.search(message)
    if group_bat:
        return group_bat.group()


def greedy_search(message):
    match_bat = re.compile(r'Bat(wo)?man')
    group_bat = match_bat.search(message)
    if group_bat:
        return group_bat.group()


def split_at_comma(message):
    split_message = re.compile(', ')
    return split_message.split(message)


def pattern_at_start(message):
    welcome_message = re.compile(r'^(Hello|Hai|Good Morning|Hi)')
    group_message = welcome_message.search(message)
    if group_message:
        return group_message.group()


def substitute_word(message):
    censor_message = re.compile(r'Agent \w+', re.IGNORECASE)
    group_message = censor_message.sub('*****', message)
    return group_message


print(check_phone_no('415-555-4242'))
print(check_phone_no('Abc-123-1234'))
print(check_phone_no('123-123-123'))
print(check_phone_no('047-123-1234'))
print(check_phone_no('*12-123-1234'))
print(find_all_phone_no('Call me at 415-555                 -1011 tomorrow. 415-555-9999 is my office.'))
print(find_all_phone_no('Meet me at 1402-566 Arlington Avenue or call me at 814-098-7522'))
print(optional_words('Batbike lost a wheel'))
print(greedy_search('Batman is the hero'))
print(split_at_comma('''12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids,
                        7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves,
                        1 partridge'''))
print(pattern_at_start('Hello! How are you'))
print(pattern_at_start('He said Hello'))
print(pattern_at_start('Bye bye.. thats all'))
print(substitute_word('AGENT Alice gave the information to AGENT Charlie'))
