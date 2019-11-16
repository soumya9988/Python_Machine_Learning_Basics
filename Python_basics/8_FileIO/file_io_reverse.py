def reverse_file(path):

    """
    Function reads and display the contents of the file in reverse order.
    """
    sentence_list = []
    with open(path, 'r', errors='ignore') as f_name:
        contents = f_name.readline()
        while contents:
            sentence_list.append(contents.strip())
            contents = f_name.readline()
    print('The items in the file in reverse order are: ')
    for item in sentence_list[::-1]:
        print(item)


def count_numbers(path):
    """
    (file path) -->
    Function that accepts the file path, read the file and return the number of digits in the file
    """
    number_list = []
    with open(path, 'r', errors='ignore') as f_name:
        content = f_name.readline()
        while content:
            words = content.split()
            for word in words:
                if word.isdigit():
                    number_list.append(word)
            content = f_name.readline()
    return number_list


file_path = input('Enter the absolute path of the file to be read: ')
reverse_file(file_path)
number_list = count_numbers(file_path)
print(number_list)



