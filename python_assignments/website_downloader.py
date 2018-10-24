from bs4 import BeautifulSoup
import webbrowser
import urllib.request
import ssl
import re
list_url = []


ssl._create_default_https_context = ssl._create_unverified_context

html_file = urllib.request.urlopen("https://www.nytimes.com")
html_text = html_file.read()
html_file.close()

soup = BeautifulSoup(html_text, 'html.parser')
for link in soup.find_all('a', attrs={'href': re.compile("^http://")}):
    list_url.append(link.get('href'))
url_set = set(list_url)
for url in url_set:
    webbrowser.open(url)



