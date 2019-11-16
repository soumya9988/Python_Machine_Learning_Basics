stud_det_list = []
avg_mark_list = []
marks = []
tot_mark = 0
avg_mark = 0

with open('studentdata.txt', 'r') as io_file:

    std_data_line = io_file.readline()
    while std_data_line:

        info = std_data_line.split()

        if len(info) > 7:
            stud_det_list.append(info[0])

        marks = info[1:]
        for mark in marks:
            tot_mark += float(mark)
        avg_mark = tot_mark / (len(info) - 1)
        avg_mark_list.append([info[0], avg_mark])

        std_data_line = io_file.readline()

print('The students having more than quiz scores are', ', '.join(stud_det_list))
print('\nThe student and their avg marks are: ')
for detail in avg_mark_list:
    print(detail)

