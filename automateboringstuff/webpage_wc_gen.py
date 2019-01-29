# Open a web page and create a word cloud with the words in it
import requests
import bs4
from wordcloud import WordCloud
import matplotlib.pyplot as pyp
import re

text_webpage = ''

# Downloading the webpage
url_webpage = 'https://automatetheboringstuff.com/chapter11/'
response = requests.get(url_webpage)
try:
    response.raise_for_status()

    # Extracting all the contents of web pageusing beautiful soup
    soup_obj = bs4.BeautifulSoup(response.text, 'html.parser')

    # Getting all the hyperlinks in the page and displaying it on screen
    for hyper_link in soup_obj.findAll('a', attrs={'href' : re.compile('^https://') }):
        print(hyper_link.get('href'))

    # Getting all the headings in the page in make a word cloud
    for text_obj in soup_obj.findAll('h2'):
        text_webpage += text_obj.get_text()

    # Plotting the word cloud generator for the text extracted above
    word_cloud = WordCloud(width= 2000, height= 1000,
                           background_color='cyan', min_font_size= 20).generate(text_webpage)

    pyp.imshow(word_cloud)
    pyp.axis('off')
    pyp.show()
    pyp.close()

except Exception as exc:
    print('Error while downloading the webpage.. %s' % exc)