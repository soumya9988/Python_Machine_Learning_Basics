import re


def password_detector(password):
    """
    (string) --> Boolean
    Accepts a password string and check if it contais:
    - at least one digit
    - Both uppercase and lowercase alphabet
    >>> password_detector(Ambhs12)
    True
    >>> password_detector(123)
    False
    >>> password_detector(password)
    False
    """

    match_upper = re.compile(r'[A-Z]')
    check1 = bool(match_upper.search(password))
    match_lower = re.compile(r'[a-z]')
    check2 = bool(match_lower.search(password))
    match_number = re.compile(r'[0-9]')
    check3 = bool(match_number.search(password))
    return check1 and check2 and check3


print(password_detector('123'))
print(password_detector('password'))
print(password_detector('Ppassword'))
print(password_detector('12aA'))
print(password_detector('Ambhs12'))
