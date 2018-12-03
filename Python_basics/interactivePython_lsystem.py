def char_change(c):
    """
    (char) --> string
    Function that accept a character c and trasnforms it into a string based on the below rule
    A --> B, B --> AB
    >>> char_change(A)
    B
    >>> char_change(B)
    AB
    """
    if c == 'A':
        return 'B'
    elif c == 'B':
        return 'AB'
    else:
        return c


def process_string(pattern):
    """
    (string) --> string
    Accepts a string pattern and calls the char_change function to modify the string into a new string called
    new_pattern
    >>>process_string(ABB)
    BABAB
    >>> process_string(ABBABB)
    BABABBABAB
    """
    new_pattern = ""
    for char in pattern:
        new_pattern = new_pattern + char_change(char)
    return new_pattern


def make_pattern(axiom, no_of_times):
    """
    (char, int) --> string
    Function accepts the starting char for Lsystem called Axiom usually 'A' and the number of times the transformation
    has to take place and return the pattern generated.
    >>> make_pattern('A',9)
    BABABBABABBABBABABBABABBABBABABBABBABABBABABBABBABABBAB
    >>> make_pattern('A', 3)
    BAB
    """
    old_pattern = axiom
    new_pattern = ""
    for i in range(no_of_times):
        new_pattern = process_string(old_pattern)
        old_pattern = new_pattern
    return new_pattern


if __name__ == '__main__':
    for i in range(10):
        print(make_pattern('A', i))

