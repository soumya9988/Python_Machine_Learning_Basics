
from datetime import datetime
from datetime import timedelta
fmt = '%m:%d:%Y %H:%M:%S'
log_list = []
with open('logfile_password.txt') as file:
    log_list = [line.rstrip() for line in file]


for line in log_list:
    line = line.split(" ")
    line_time = line[1] + " " + line[2]
    delta_time = datetime.strptime(line_time, fmt) + timedelta(minutes= 30)
    print(delta_time)

import re
import datetime

match_record = re.compile(r"^[^ ]+ - (C[^ ]*) \[([^ ]+)").match
strptime = datetime.datetime.strptime

f = open("very/big/log", "rb")

for line in f:
    match = match_record(line)
    if match is not None:
        user, str_time = match.groups()
        time = strptime(str_time, "%d/%b/%Y:%H:%M:%S")
        print user, repr(time)