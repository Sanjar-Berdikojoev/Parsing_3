import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt

URL = 'https://inai.kg/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
}

@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS)
    return req


@csrf_exempt
def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='post')
    inai_news = []

    for item in items:
        inai_news.append(
            {
                'image': item.find('img').get('src'),
                'title': URL + item.find('a').get('href'),
                'title_text': item.find('div', class_='post-body').get_text(),
                'description': item.find('div', class_='post-body').find('p').get_text(),
                'published_data': item.find('div', class_='mt-3').find('span').get_text(),
            }
        )
    return inai_news

@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        inai_news_1 = []
        for page in range(0, 1):
            html = get_html(f'https://inai.kg/', params=page)
            inai_news_1.extend(get_data(html.text))
        return inai_news_1
    else:
        raise Exception('Error in parser func........')