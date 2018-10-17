poem = '''The woods are lovely, dark and deep,   
But I have promises to keep,   
And miles to go before I sleep,   
And miles to go before I sleep.'''

with open("text_poem.txt", 'w+t') as my_file:
    my_file.write(poem)
print(my_file.closed)

with open('text_poem.txt', 'r') as poem_txt:
    while True:
        line = poem_txt.readline()
        print(line, end='')
        if len(line) <= 0:
            break
    print('\n')
