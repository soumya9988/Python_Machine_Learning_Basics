import urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore the certificate error:
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the url to be read: ')
req = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(req, 'html.parser')

comments = soup.findAll(class_ = 'comments')
sum_comments = 0
for comment in comments:
    sum_comments += int(comment.text)

print(sum_comments)





