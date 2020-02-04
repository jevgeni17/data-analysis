# bookvoed.ee scraper
import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrap(page='https://bookvoed.ee/search?q=%D0%BC%D0%B0%D1%80%D1%82%D0%B8%D0%BD+%D0%B8%D0%B4%D0%B5%D0%BD'):
    page = requests.get(page)
    soup = BeautifulSoup(page.content, 'html.parser')
    items = soup.findAll(class_='o-row')
    print(items)
    #print(week[0].find(class_='title').get_text())
    #print(week[0].find(class_='author').get_text())
    q = items[0].find(class_='buy')
    #print(q.find('span').get_text())

    titles = [item.find(class_='title').get_text() for item in items]
    authors = [item.find(class_='author').get_text() for item in items]
    price = [q.find('span').get_text() for q in items]

    books_stuff = pd.DataFrame(
        {
            'title': titles,
            'author': authors,
            'price': price,
        })
    print(books_stuff)

    books_stuff.to_csv('x.csv', encoding="cp1251")

scrap()
