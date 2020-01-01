import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://bookvoed.ee/search?q=%D0%B1%D0%B5%D0%BB%D1%8B%D0%B9+%D0%BA%D0%BB%D1%8B%D0%BA')
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

books_stuff.to_csv('books.csv', encoding="cp1251")