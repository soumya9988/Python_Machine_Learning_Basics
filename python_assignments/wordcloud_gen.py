from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from wordcloud import WordCloud
from os import path

str = ''
cur_dir =  path.dirname(__file__)

url = "http://taaism.com/resumecv-writing-12-things-for-a-fresher-to-ponder/"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html_text = urlopen(req).read()
webpage = html_text.decode('utf-8')
soup = BeautifulSoup(webpage, 'html.parser')
for a in soup.find_all(class_="entry-content"):
    for b in a.find_all("ol"):
        str += b.text

wc = WordCloud(background_color='white',
               max_words= 250)
wc.generate(str)
wc.to_file(path.join(cur_dir, "resume_cloud.png"))
