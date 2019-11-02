# fname = input("Enter file name: ")
# fh = open(fname)
# total = 0
# count = 0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:") :
#         continue
#     else:
#         index = int(line.find('0'))
#         number = float(line[index:])
#         total += number
#         count += 1
#
# average = total/count
# print("Average spam confidence:", average)
#
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(len(c))
#
# fname1 = input("Enter file name: ")
# fh1 = open(fname1)
# set_words = []
# for line1 in fh1:
#     line1 = line1.rstrip().split()
#     for word in line1:
#         if word not in set_words:
#             set_words.append(word)
# set_words.sort()
# print(set_words)

# count = 0
# fname = input("Enter file name: ")
# if len(fname) < 1 :
#     fname = "mbox-short.txt"
# with open(fname, 'r', errors='ignore') as f_name:
#     content = f_name.readline()
#     while content:
#         list_words = []
#         if content.startswith('From '):
#             list_words = content.split()
#             address = list_words[1]
#             print(address)
#             count += 1
#         content = f_name.readline()
#
# print("There were", count, "lines in the file with From as the first word")

# fname = input("Enter file name: ")
# if len(fname) < 1 :
#     fname = "mbox-short.txt"
#
# fh = open(fname)
# count = 0
# dict_sender = {}
# for line in fh:
#     if line.startswith('From '):
#         address = line.split()
#         email = address[1]
#         dict_sender[email] = dict_sender.get(email, 0) + 1
#
# max_key = None
# max_value = 0
# for key, value in dict_sender.items():
#     if max_value < value:
#         max_key = key
#         max_value = value
#
# print(max_key, max_value)

# fname = input("Enter file name: ")
# if len(fname) < 1 :
#     fname = "mbox-short.txt"
#
# fh = open(fname)
# count = 0
# dict_sender = {}
# for line in fh:
#     if line.startswith('From '):
#         address = line.split()
#         email = address[1]
#         dict_sender[email] = dict_sender.get(email, 0) + 1
#
# list_sender = sorted([(v, k) for k, v in dict_sender.items()], reverse=True)
# for sender in list_sender[:5]:
#     print(sender[0], sender[1])

fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
dict_hours = {}
for line in fh:
    if line.startswith('From '):
        content = line.split()
        time = content[5]
        hour = time.split(':')[0]
        dict_hours[hour] = dict_hours.get(hour, 0) + 1
list_hours = sorted([(k, v) for k, v in dict_hours.items()])
for hour in list_hours:
    print(hour[0], hour[1])




