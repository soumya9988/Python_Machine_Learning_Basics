import requests
import bs4
import re
import webbrowser

list_url= []

url_parent = 'https://www.carters.com'
response = requests.get(url_parent)
try:
    response.raise_for_status()
    soup_obj = bs4.BeautifulSoup(response.text, 'html.parser')
    with open('all_hyper_links.txt', 'w') as file:
        file.write(soup_obj.text)
    for link in soup_obj.findAll('a', attrs={'href': re.compile('^https://')}):
        list_url.append(link.get('href'))
    print(len(list_url))
    max_page = min(10, len(list_url))
    for index in range(max_page):
        webbrowser.open(list_url[index])

except Exception as exc:
    print('Error while downloading.. %s' % exc)
