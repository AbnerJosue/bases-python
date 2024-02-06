import lxml
import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/')
sopa = bs4.BeautifulSoup(resultado.text,'lxml')

print(sopa.select('title')) # retorna una lista de [title]
print(sopa.select('h1')) # retorna una lista de [h1 con sus valores]

# obtener solo el texto y no la etiqueta 
print(sopa.select('title')[0].getText())

parrafo_especial = sopa.select('h2')[0].getText()
print(f'parrafo especial {parrafo_especial}')


columa = sopa.select('.r-snippetized')

for p in columa: 
    print(p.getText())