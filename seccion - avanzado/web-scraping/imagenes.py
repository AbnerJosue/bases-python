import lxml
import bs4
import requests

resultado = requests.get('https://www.escueladirecta.com/?_ga=2.16704817.620857383.1707194126-1040836923.1707194126')

sopa = bs4.BeautifulSoup(resultado.text,'lxml')
imagenes = sopa.select('.course-box-image')[0]['src']
imagen_curso = requests.get(imagenes)

# wb write binari
f = open('mi_imagen.jpg', 'wb')
f.write(imagen_curso.content)
f.close()
