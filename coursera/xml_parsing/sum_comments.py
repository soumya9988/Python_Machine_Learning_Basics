import urllib.request, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
print('Retrieving', url)
req = urllib.request.urlopen(url, context=ctx)

data = req.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
list_comment = tree.findall('comments/comment')
print('Count:', len(list_comment))

sum_comment = 0
for comment in list_comment:
    sum_comment += int(comment.find('count').text)

print('Sum:', sum_comment)



