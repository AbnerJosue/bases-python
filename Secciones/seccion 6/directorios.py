import os 

ruta = os.getcwd() # conocer el lugar en donde se encuentra el directorio
print(ruta)
# -----------------
ruta2 = os.chdir('C:\\Users\\josue\\Estudios\\python') # cambiar de directorio 
archivo = open('otro_archivo.txt')
print(archivo.read())
print(ruta2)

# crear directorio 
# ruta3 = os.makedirs('C:\\Users\\josue\\Estudios\\python\\nuevo.txt')

ruta4 = os.path.basename('C:\\Users\\josue\\Estudios\\python\\Python-Curso\\file\\seccion 6\\prueba.txt')
print(ruta4)

ruta4 = os.path.dirname('C:\\Users\\josue\\Estudios\\python\\Python-Curso\\file\\seccion 6\\prueba.txt')
print(ruta4)

# eliminar la carpeta 
# ruta5 = os.rmdir('C:\\Users\\josue\\Estudios\\python\\nuevo.txt')

# pathlib
from pathlib import Path

carpeta = Path('/Users/josue/Estudios/python') / 'otro_archivo.txt'
mi_archivo = open(carpeta)
print(mi_archivo.read())