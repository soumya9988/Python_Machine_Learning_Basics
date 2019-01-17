"""
Chapter 6 - Manipulating Strings of Automate the Boring Stuff
Exercise : Table printer
printTable() takes a list of lists of strings and displays it in a well-organized table with each column
right-justified. Assume that all the inner lists will contain the same number of strings.

"""


def printTable(list_words):
    max_len_word = []

    # Getting the length of longest word in each row in the list of words
    for words in list_words:
        len_list_words = []
        for word in words:
            len_list_words.append(len(word))
        max_len_word.append(max(len_list_words))

    # Formatting the table by right justifying each word against the longest word
    pretty_list = []
    for counter in range(len(list_words[0])):
        word_row = ''
        for index in range(len(list_words)):
            col_width = max_len_word[index]
            word_row += ( list_words[index][counter].rjust(col_width) + '  ')
        pretty_list.append(word_row)

    # Printing the words
    print('The pretty formatted list of words are as below: ')
    for items in pretty_list:
        print(items)


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose'],
             ['Mercury', 'Venus', 'Earth', 'Mars']]
printTable(tableData)
