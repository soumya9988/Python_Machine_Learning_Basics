import requests
import bs4
import os

dir_name = os.path.join(os.getcwd(), 'imgur_dir')
os.makedirs(dir_name, exist_ok=True)

base_url = 'https://imgur.com/search/score?q=alleppey'
response = requests.get(base_url)
try:

    response.raise_for_status()
    soup_obj = bs4.BeautifulSoup(response.text, 'html.parser')

    for image in soup_obj.findAll('a', attrs={'class':'image-list-link'}):
        image_url = 'http:' + image.find('img')['src']
        image_res = requests.get(image_url)
        try:
            image_res.raise_for_status()
            print('Downloading image', image_url)

            image_name = os.path.basename(image_url)
            file_name = os.path.join(dir_name, image_name)
            with open(file_name, 'wb') as image_file:
                for content in image_res.iter_content(1000000):
                    image_file.write(content)
        except:
            print('Error downloading image....')


except Exception as ex:
    print('Error while opening imgur... %s' % ex)