"""
Chapter 11 – Web Scraping
1. Gets search keywords from the command line arguments.
2. Retrieves the search results page.
3. Opens a browser tab for each result.
"""

import requests
import bs4
import webbrowser
import sys

google_link = 'https://www.google.com/'

# Downloading the webpage for the search term in system argument
search_term = sys.argv[1:]
full_url ='https://www.google.com/search?client=safari&rls=en&q=' + ''.join(search_term)
response = requests.get(full_url)

try:

    # Getting the status and checking for error while downloading the webpage
    response.raise_for_status()

    # Extracting the contents of html page
    soup_obj = bs4.BeautifulSoup(response.text, 'html.parser')
    dir_obj = soup_obj.select('.r a')

    # Getting the top search results url and opening a browser for each of them
    for i in range(len_dir_obj):
        search_result = dir_obj[i].get('href')
        webbrowser.open(google_link + search_result )


except Exception as exc:
    print('There was an error while downloading... %s' % exc)