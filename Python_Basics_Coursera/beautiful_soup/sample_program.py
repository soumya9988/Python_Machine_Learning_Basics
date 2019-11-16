import urllib.request, urllib.error

req = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
word_count= {}
for line in req:
    line = line.decode().split()
    for word in line:
        word_count[word] = word_count.get(word, 0) + 1

max_word_count = sorted([(v, k) for k, v in word_count.items()], reverse=True)
print(max_word_count[0][1])


