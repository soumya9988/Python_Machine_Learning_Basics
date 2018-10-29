from bs4 import BeautifulSoup
import webbrowser
import urllib.request
import urllib.error
import ssl
from time import sleep
import re

# LList to store all the links in a website
list_url = []


ssl._create_default_https_context = ssl._create_unverified_context
try:

    # Downloading the raw html code of the given url
    url = input('Enter the url of the website..')
    html_file = urllib.request.urlopen(url)
    html_text = html_file.read()
    html_file.close()


    # loading the html into BeautifulSoup object to get all the links
    soup = BeautifulSoup(html_text, 'html.parser')
    for link in soup.find_all('a', attrs={'href': re.compile("^http://")}):
        list_url.append(link.get('href'))
    url_set = set(list_url)

    print(url_set)
    sleep(20)
    # finally, opening the urls extracted in the above step
    for url in url_set:
        webbrowser.open(url)

except urllib.error.HTTPError:
    print('HTTP Error..')

except urllib.error.URLError:
    print('Page not found')



