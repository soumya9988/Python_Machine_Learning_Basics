spam = {'Alice' : 30,
        'planets' : ['mars', 'venus', 'earth', 'pluto'],
        'pi' : 3.14,
        1: 13}

# Key, values and items in dictionary
print(spam.keys())
print(spam.values())
print(spam.items())

# setdefault method in dict
spam.setdefault('colour', 'black')
print(spam)
spam.setdefault('colour', 'pink')
print(spam)

# get() method in dict with default value
print(spam.get('Alice', 50))
print(spam.get('Alan', 50))
