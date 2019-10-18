import requests
import bs4
import re


def get_word_definition(word):
    count = 1

    # Calling the dictionary.com
    base_url = 'https://www.dictionary.com/browse/' + word
    response = requests.get(base_url)
    soup_obj = bs4.BeautifulSoup(response.text, 'html.parser')
    try:

        # Getting all the elements in the synonym container
        span_elem = soup_obj.find(class_="css-1o58fj8 e1hk9ate4")
        word_list = span_elem.find_all(class_="one-click-content css-1p89gle e1q3nk1v4")
        print('Possible meanings of the word are: \n')
        for elem in word_list:
            text_s = elem.text
            text_s = text_s.split(":", maxsplit=1)[0]
            print(str(count) + '. ' + text_s.capitalize())
            count += 1

    except Exception as err:

        # In case there is no valid word, suggest the best possible alternatives for the word.
        print('We couldn\'t find an exact match for the word!\nPlease enter one from the below suggestion')
        for hyper_link in soup_obj.findAll('a', attrs={'href': re.compile('/browse')}):
            print(hyper_link.text)
        word = input('Enter the word: ')
        get_word_definition(word)


word = input('Enter the word: ')
get_word_definition(word)
