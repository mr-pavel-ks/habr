import requests
from bs4 import BeautifulSoup
KEYWORDS = ['дизайн', 'фото', 'web', 'python']
url = 'https://habr.com/ru/all/'
response = requests.get(url)
soup = BeautifulSoup(response.text ,'html.parser')
for article in soup.find_all('article', class_ ='post'):
    hubs = article.find_all('div', class_ = 'post__text')

    hubs_text = list(map(lambda x: x.text.lower(), hubs))
    for kw in KEYWORDS:
        if kw in hubs_text[0]:
            title_element = article.find('a', class_ = 'post__title_link')
            title = title_element.text
            link = title_element.attrs.get('href')
            time_element = article.find('span', class_= 'post__time')
            time = time_element.text
            print(f'{time} - {title} - {link}')





