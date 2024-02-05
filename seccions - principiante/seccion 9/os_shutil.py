import os 
import shutil
import send2trash

# archivo = open('curso.txt', 'w')
# archivo.write('Texto de prueba')
# archivo.close()
# print(os.listdir())

# mover 
# shutil.move('curso.txt', 'C:\\Users\\josue\\Desktop')

# eliminar un archivo en una ruta 
#os.rmdir
# eliminar carpeta vacia
#os.rm
# rmt eliminar todo lo de la ruta
# shutil.rmt esto es irreversible

# lo manda al basurero al borrar
# send2trash.send2trash('curso.txt')

# recorrer todos los directorios 

ruta = 'C:\\Users\\josue\\Estudios\\python\\Python-Curso'


for carpeta,subcarpeta, archivo in os.walk(ruta): 
    print(f'En la carpeta: {ruta}')
    print(f'Las carpetas son: ')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son: ')
    for arch in archivo: 
        print(f'\t{arch}')
    print('\n')



# PREGUNTAS 
    
# Es en general buena idea utilizar el método rmtree() del módulo shutil para deshacernos rápidamente de las carpetas innecesarias, ya que es eficiente liberando memoria.
    # Por lo general, querrás evitar cualquier paso en falso utilizando 
    # el método rmtree() del módulo shutil, ya que los archivos se eliminan sin 
    # dejar rastros ni pasar por la papelera de reciclaje, por lo que no podrás recuperar tu información si te equivocas.

