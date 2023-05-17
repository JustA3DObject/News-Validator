import requests
from bs4 import BeautifulSoup

page_link = []
articles_list = []

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36",
           "X-Amzn-Trace-Id": "Root=1-62d8036d-2b173c1f2e4e7a416cc9e554", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
           "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-GB", }


i = 1
while (i < 51):
    page_link = (f'https://www.hindustantimes.com/world-news/page-{i}')

    i = i+1
    try:
        page = requests.get(page_link, headers=headers)
        page.raise_for_status()

        if page.status_code == 200:
            soup1 = BeautifulSoup(page.text, "html.parser")
            soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

        articles = soup2.find('section', id="dataHolder").find_all(
            'div', class_="cartHolder")

        articles_list.extend(articles)

    except Exception as e:
        print(e)
print(len(articles_list))
