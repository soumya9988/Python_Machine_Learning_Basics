def displayInventory(inventory):
    """
    (dictionary string : int) --> None

    Function that accepts a dictionary of Inventory where the item name is the key and
    number of each item is the value.
    It will print the no of items and the item name.
    It will also print the total number of items in the Inventory
    >>> stuff = {'rope': 1, 'torch': 6}
    >>> displayInventory(stuff)
    Inventory:
    1 rope
    6 torch
    Total number of items: 7

    """
    no_of_items = 0
    print('Inventory:')
    for items in inventory:
        print(inventory[items], items)
        no_of_items += inventory[items]
    print('Total number of items:', no_of_items)


def addToInventory(inventory, addedItems):
    """
    (dictionary, List of string) --> dictionary
    Function will accept a dictionary containing inventory details and a list of addedItems.
    It will update the dictionary with the addedItems list and will return the updated dictionary.
    >>> inv = {'gold coin': 42, 'rope': 1}
    >>> dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    >>> inv = addToInventory(inv, dragonLoot)
    Inventory:
    45 gold coin
    1 rope
    1 ruby
    1 dagger
    """
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
