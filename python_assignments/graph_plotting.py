import datetime
from matplotlib.backends.backend_pdf import PdfPages
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import requests


# Pie chart to show the items purchased and the amount
def pie_chart_item_amount(pdf):
    amount = [9.5, 18, 32.5, 17, 23]
    items = ['Flour', 'Butter', 'Sugar', 'Berries', 'Chocolates']
    plt.title('Items Vs. Amount Spend')
    plt.pie(amount, labels=items, startangle=30, autopct='%.1f$')
    pdf.savefig()  # saves the current figure into a pdf page
    plt.close()


# A bar chart to represent the height in inches and the suitable shoe size
def height_shoe_size(pdf):
    height = [60, 61, 62, 63, 64, 65, 66, 67, 68]
    shoe_size = [3, 3, 4, 4, 5, 5, 6, 6, 7]
    plt.bar(height, shoe_size, label='Size', color='b')
    plt.legend()
    plt.xlabel('Height in inches')
    plt.ylabel('Shoe size')
    plt.title('Height Vs. Shoe size')
    pdf.savefig()
    plt.close()


# Word cloud generator for a web page
def word_cloud_generator(pdf):
    words_webpage = ''
    stop_words = set(STOPWORDS)

    url = "http://taaism.com/resumecv-writing-12-things-for-a-fresher-to-ponder/"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html_text = urlopen(req).read()
    webpage = html_text.decode('utf-8')
    soup = BeautifulSoup(webpage, 'html.parser')
    for a in soup.find_all(class_="entry-content"):
        for b in a.find_all("ol"):
            words_webpage += b.text

    wc = WordCloud(background_color='gray',
                   max_words=250,
                   stopwords=stop_words).generate(words_webpage)
    plt.axis('off')
    plt.imshow(wc)
    pdf.savefig()
    plt.close()


# To get the temperature of Plano and plot it in a line graph
def weather_report_plano(pdf):
    # Getting the start date
    day = datetime.date.today() - datetime.timedelta(days=7)

    # Empty list to hold the x and y coordinates of the graph
    dict_temp = {}

    # Loop to get the temperatures of the past 7 days using API call to dark sky
    for i in range(7):
        # Formatting the date
        new_date = (day + datetime.timedelta(days=i)).strftime('%Y-%m-%d')
        search_date = new_date + 'T00:00:00'

        # API call to dark sky
        response = requests.get(
            "https://api.darksky.net/forecast/32f18c758a622f85268e110f29e67f9d/33.0198,-96.6989," + search_date + "?exclude=daily")
        json_res = response.json()

        # Getting the temperature
        formatted_data = (json_res['hourly']['data'][0]['temperature'])
        date_format = (day + datetime.timedelta(days=i)).strftime('%d-%m')
        dict_temp[date_format] = formatted_data

    # Plotting the graph
    plt.plot(dict_temp.keys(), dict_temp.values(), linewidth=4)
    plt.xlabel('Date')
    plt.ylabel('Temperature in F')
    plt.title('Temperature in Plano for past 7 days')
    pdf.savefig()
    plt.close()


# Create the PdfPages object to which we will save the pages:
with PdfPages('multipage_pdf.pdf') as pdf:

    # Calling the modules for getting the plots
    weather_report_plano(pdf)
    pie_chart_item_amount(pdf)
    height_shoe_size(pdf)
    word_cloud_generator(pdf)

    # Set the file's metadata via the PdfPages object:
    d = pdf.infodict()
    d['Title'] = 'Multipage PDF'
    d['Author'] = u'Soumya Narayanan'
    d['CreationDate'] = datetime.datetime(2018, 10, 25)
    d['ModDate'] = datetime.datetime.today()