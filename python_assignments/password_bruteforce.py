from datetime import datetime
from datetime import timedelta

log_dict = {}
fmt = '%m:%d:%Y %H:%M:%S'

login = int(input('Enter the number of failed login for brute forcing: '))
minute = int(input('Enter the time limit: '))

with open('logfile_password.txt') as file:
    log_list = [line.rstrip() for line in file]


for line in log_list:
    counter = 0
    line = line.split(" ")
    date_time = line[1] + " " + line[2]
    line_time = datetime.strptime(date_time, fmt)
    delta_time = line_time + timedelta(minutes= minute)

    for itm in log_list:
        itm = itm.split(" ")
        itm_time = itm[1] + " " + itm[2]
        item_time = datetime.strptime(itm_time, fmt)
        if line_time <= item_time < delta_time and itm[0] == line[0]:
            counter += 1
    if counter >= login and line[0] not in log_dict:
        log_dict[line[0]] = counter


with open('output_file.txt', 'w') as op_file:
    for line in log_dict:
        login_det = 'Number of failed login : ' + str(log_dict[line]) + '\n'
        op_file.write(login_det)
        attacker = ' Detected brute force attacks : ' + str(line) + '\n'
        op_file.write(attacker)
        op_file.write('\n')
