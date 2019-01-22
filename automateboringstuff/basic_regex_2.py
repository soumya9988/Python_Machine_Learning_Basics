import re


def name_matching(name):
    name_format = re.compile(r'^[A-Z][a-z]+ Nakamoto')
    check_name = name_format.search(name)
    if check_name:
        return check_name.group()


def digit_with_comma(number):
    number_format = re.compile(r'(^\d{1,3})(,\d{3})*$')
    check_no = number_format.search(number)
    return bool(check_no)


def alice_bob_carol(sentence):
    sent_format = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.$', re.IGNORECASE)
    check_format = sent_format.search(sentence)
    return bool(check_format)


print('Name check')
print(name_matching('Satoshi Nakamoto'))
print(name_matching('Alice Nakamoto'))
print(name_matching('satoshi Nakamoto'))
print(name_matching('Mr. Nakamoto'))
print(name_matching('Nakamoto'))
print(name_matching('Satoshi nakamoto'))
print(name_matching('W123 Nakamoto'))
print(name_matching('Robocop Nakamoto'))
print('Number format')
print(digit_with_comma('42'))
print(digit_with_comma('1,234'))
print(digit_with_comma('6,345,123'))
print(digit_with_comma('12,34,567'))
print(digit_with_comma('1234'))
print('Sentence check')
print(alice_bob_carol('Alice eats apples.'))
print(alice_bob_carol('Bob pets cats.'))
print(alice_bob_carol('Alice throws Apples.'))
print(alice_bob_carol('BOB EATS CATS.'))
print(alice_bob_carol('ALICE THROWS FOOTBALLS.'))
print(alice_bob_carol('Robocop eats apples.'))
print(alice_bob_carol('Carol eats 7 cats.'))







