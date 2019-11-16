import requests
from bs4 import BeautifulSoup
import re

content = ''
response = requests.get('https://www.geeksforgeeks.org/python-language-introduction/')
try:
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')

    for a in soup.find_all('div', attrs= {'class': 'entry-content'}):
        for b in a.find_all("p"):
            content += b.text + '\n'

    code = soup.find_all('div', {'class': re.compile(r'^line number')})
    for c in code:
        content += c.text + '\n'

    # Getting all the recommended links in the web page
    for recommend_links in soup.find_all('div', {'class': 'recommendedPostsDiv'}):
        for list_items in recommend_links.find_all('li'):
            content += list_items.find('a', attrs= {'href': re.compile(r'^https')}).get('href') + '\n'

    # Writing the contents from the web page into a text file
    with open('content.txt', 'w') as write_file:
        write_file.write(content)

except Exception as ex:
    print(ex)
