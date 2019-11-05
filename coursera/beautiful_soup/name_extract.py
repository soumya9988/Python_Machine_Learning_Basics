import urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore the certificate error:
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: ')) + 1
position = int(input('Enter position: ')) - 1


for i in range(count):
    print('Retrieving: ', url)
    req = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(req, 'html.parser')
    names = []
    for links in soup.findAll('a', attrs={'href': re.compile(r'^http')}):
        names.append(links.text)
    new_name = names[position]

    url = 'http://py4e-data.dr-chuck.net/known_by_' + new_name + '.html'
