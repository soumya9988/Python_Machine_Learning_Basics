def list_to_string(list_val):
    """ (list of string) -> string

        Takes a list value and returns a string with all the items
        separated by a comma and a space, with 'and' inserted before the last item.

        >>> list_to_string(['apples', 'bananas', 'tofu', 'cats'])
        'apples, bananas, tofu, and cats'
    """
    full_string = list_val[0]
    for item in list_val[1:-1]:
        full_string = full_string + ', ' + item
    full_string = full_string + ' and ' + list_val[-1]
    return full_string


spam = ['apples', '129' , 'broccoli', 'bananas', '3.14' , 'cats', 'dogs', 'pigeons']
print(list_to_string(spam))