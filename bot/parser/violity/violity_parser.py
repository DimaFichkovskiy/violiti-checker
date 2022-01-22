import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'accept': '*/*'}


def get_data_on_lot(violity_url):
    counter = 1
    photo_url = list()
    html = requests.get(violity_url, headers=HEADERS).text
    soup = BeautifulSoup(html, "lxml")
    name_lot = soup.find('h1', class_='page_title').text
    finish_date = soup.find('div', class_='finish_time').find('span').text.split(', ').pop(0)
    finish_time = soup.find('div', class_='finish_time').find('span').text.split(', ').pop(1)

    current_price_UAH = soup.find('div', class_='c_price_button').find('span').text
    current_price_USD = soup.find('div', class_='cur_price').find('p').text

    photos = soup.find('div', class_='slider_frame')
    photos_url = photos.find_all('img')
    for photo_data in photos_url:
        if counter <= 10:
            photo_url.append(photo_data.get('data-src'))
            counter += 1

    data_about_lot = dict(
        {
            'name': name_lot,
            'finish_date': finish_date,
            'finish_time': finish_time,
            'current_price_UAH': current_price_UAH,
            'current_price_USD': current_price_USD,
            'photos_url': photo_url
        }
    )
    return data_about_lot

if __name__ == '__main__':
    violity_url="https://violity.com/109146616-novye-chasy-znaki-zodiaka-slava-sssr/?utm_source=interesting_items&utm_medium=novye-chasy-znaki-zodiaka-slava-sssr&utm_campaign=24"
    get_data_on_lot(violity_url)
