import webbrowser
import requests
import bs4

# To open a web browser
webbrowser.open('https://weather.com/weather/tenday/l/Plano+TX+USTX1060:1:US')

# To download the web page
response = requests.get('https://automatetheboringstuff.com/chapter12/')
try:
    response.raise_for_status()
    print(response.url, response.links, response.status_code, response.text[0:500])
    print(requests.codes.ok == response.status_code)
except Exception as excp:
    print('There was a problem while downloading: %s' % excp)

#  Checking for errors. Always call raise_for_status() after calling requests.get().
# You want to be sure that the download has actually worked before your program continues.
err_res = requests.get('https://automatetheboringstuff.com/nochapterexist/')
try:
    err_res.raise_for_status()
except Exception as exc:
    print('There was a problem while downloading: %s' % exc)

# Beautiful Soup is a module for extracting information from an HTML page.
soup_obj = bs4.BeautifulSoup(response.text)
print(soup_obj.text)

# You can retrieve a web page element from a BeautifulSoup object by calling the select()method
print(soup_obj.select('#author'), soup_obj.select('div'))

with open('example.html', 'r') as html_page:
    html_text = html_page.read()
    content = bs4.BeautifulSoup(html_text, features='lxml')
print(content)

