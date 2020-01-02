import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrap(page,file_name='books.csv'):
    page = requests.get(page)
    soup = BeautifulSoup(page.content, 'html.parser')
    items = soup.findAll(class_='o-row')

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

    books_stuff.to_csv(file_name, encoding="cp1251")
    
scrap('https://bookvoed.ee/search?q=%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5', 'hi.csv')
    