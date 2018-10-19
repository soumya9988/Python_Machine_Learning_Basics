name_dict = {}
with open('name_list.txt', 'r') as name_file:
    while True:
        line = name_file.readline()
        if len(line) <= 0:
            break
        else:
            line = line.strip()
            if line in name_dict:
                name_dict[line] += 1
            else:
                name_dict[line] = 1
    print(name_dict)


