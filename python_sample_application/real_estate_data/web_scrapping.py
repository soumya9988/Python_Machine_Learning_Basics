# Importing the libraries
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# Setting the base url of the website to the first page of search result
base_url = 'https://www.tripadvisor.com/Hotels-g56463-Plano_Texas-Hotels.html#BODYCON'
list_of_hotels = []
while True:
    response = requests.get(base_url)
    try:
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Getting the hotel name and individual link to hotels
        for details in soup.find_all('div', {'class': 'listing collapsed'}):
            hotel_det = {}
            try:
                # Hotel name
                hotel_det['Title'] = details.find('div', {'class': 'listing_title'}).text
            except:
                # if detail is not found, set the value to NaN
                hotel_det['Title'] = None

            # URL to the hotel details
            hotel_det['Link'] = 'https://www.tripadvisor.com' + \
                                details.find('a', attrs={'href': re.compile(r'^/Hotel_Review')}).get('href')

            # Price per day
            try:
                hotel_det['Price'] = details.find('div', {'data-clickpart': 'chevron_price'}).text
            except:
                hotel_det['Price'] = None

            # Details like top rated/ breakfast options etc
            attraction = []
            for speciality in details.find_all('div', {'class': re.compile(r'^ui_ribbon')}):
                attraction.append(speciality.text)
            if attraction:
                hotel_det['Attraction'] = ' & '.join(attraction)
            else:
                hotel_det['Attraction'] = None

            # Special offers like WiFi and pool
            offer_text = []
            try:
                offers = details.find('ul', {'class': 'icons_list easyClear vertical'})
                for offer in offers.find_all('li', {'class': 'hotel_icon'}):
                    offer_text.append(offer.text)
                hotel_det['Offers'] = ' & '.join(offer_text)
            except:
                hotel_det['Offers'] = None

            list_of_hotels.append(hotel_det)

        # Getting the url for next page of hotels
        page_no = soup.find('div', attrs={'class': 'unified ui_pagination standard_pagination ui_section listFooter'})
        next_page = page_no.find('a', attrs={'class': 'nav next taLnk ui_button primary'})
        try:
            base_url = 'https://www.tripadvisor.com' + next_page.get('href')
            print(base_url)
        except:
            break

    except Exception as ex:
        print('Error while downloading webpage: %s' % ex)
        break

    # Finally, appending the details into a csv file
    dataframe = pd.DataFrame(list_of_hotels)
    dataframe.set_index('Title')
    dataframe.to_csv('list_of_hotels.csv')

