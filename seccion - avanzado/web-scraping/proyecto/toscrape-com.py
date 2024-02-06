import lxml
import bs4
import requests

# crear ul sin numero de pagina
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# lista de titulos con cuatro estrellas

titles_rating_heigth = []

# iterar paginas 

for pagina in range(1,51):
    # crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    result = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(result.text, 'lxml')

    # seleccion de libros 
    books = sopa.select('.product_pod')
    # iterar en los libros

    for book in books:
        # chequear estrellas
        if len(book.select('.star-rating.Four')) != 0 or len(book.select('.star-rating.Five')) != 0 :
            # guardar titulo en variable 
            title = book.select('a')[1]['title']
            # agregar libro a la lista
            titles_rating_heigth.append(title)

for t in titles_rating_heigth: 
    print(t)
    