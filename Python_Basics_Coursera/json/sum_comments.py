import urllib.request, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'
print('Retrieving', url)
req = urllib.request.urlopen(url, context=ctx)

data = req.read()
print('Retrieved', len(data), 'characters')

json_data = json.loads(data)
comments = json_data['comments']
print('Count:', len(comments))
sum_comments = 0
for name in comments:
    sum_comments += int(name['count'])

print('Sum:', sum_comments)

