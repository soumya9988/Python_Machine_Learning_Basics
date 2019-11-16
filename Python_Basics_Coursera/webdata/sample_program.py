# import re

# list_num = []
# with open('word.txt', 'r') as ip:
#     content = ip.readline()
#     while content:
#         line = content.rstrip()
#         for pattern in re.findall(r'X-DSPAM-Confidence: ([0-9]*\.[0-9]*)', line):
#             list_num.append(float(pattern))
#         content= ip.readline()
#
# print('Maximum: ', max(list_num))

# import re
# fname = input("Enter file name: ")
# if len(fname) < 1:
#     fname = 'sum_42.txt'
# fh = open(fname)
# sum_no = sum([int(x) for x in (re.findall(r'[0-9]+', fh.read().rstrip()))])
# print(sum_no)

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://http://data.pr4e.org/intro-short.txt\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data)

mysock.close()
