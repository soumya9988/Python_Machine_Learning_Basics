def countAll(word):
    """
    (string) --> dict
    A function that accepts a word and count the number of characters in the word and return a dictionary with the
    characters and number of times it occur
    >>>countAll("banana")
    {"a":3, "b":1, "n":2}
    """
    counts = {}
    for char in word.lower():
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    return counts

print(countAll("ThiS is String with Upper and lower case Letters."))
