import requests
import bs4
import os

base_url = 'http://xkcd.com'
dir_name = os.path.join(os.getcwd(), 'comic_dir')
os.makedirs(dir_name, exist_ok=True)

for index in range(10):
    print('Downloading page', base_url, '...')
    response = requests.get(base_url)
    try:
        response.raise_for_status()
        soup_obj = bs4.BeautifulSoup(response.text, 'html.parser')
        image_obj = soup_obj.select('#comic img')
        # print(image_obj[0].attrs, '\n', image_obj[0].get('src'))
        image_url = 'http:' + image_obj[0].get('src')

        print('Downloading image', image_url, '...')
        res_url = requests.get(image_url)

        try:
            res_url.raise_for_status()
            url_name = os.path.basename(image_url)
            file_name = os.path.join(dir_name, url_name)

            with open(file_name, 'wb') as png_file:
                for content in res_url.iter_content(100000):
                    png_file.write(content)

        except Exception as exec:
            print(exec)

        prev_link = soup_obj.select('a[rel="prev"]')
        prev_url = prev_link[0].get('href')
        base_url = 'http://xkcd.com' + prev_url

    except Exception as exc:
        print('There is an error while downloading website...\n %s' % exc)