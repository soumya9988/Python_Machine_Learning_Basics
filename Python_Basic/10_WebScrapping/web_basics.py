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

except urllib.error.HTTPError:
    print('HTTP Error..')

except urllib.error.URLError:
    print('Page not found')



