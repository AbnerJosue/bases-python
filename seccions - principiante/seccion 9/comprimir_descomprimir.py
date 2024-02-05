import zipfile

mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')

mi_zip.write('mi_texto.txt')
mi_zip.write('mi_text2.txt')


mi_zip.close()



mi_zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')
mi_zip_abierto.extractall()


import shutil

carpeta_origen = 'C:\\Users\\josue\\Estudios\\python\\Python-Curso\\seccions\\seccion 9'

archivo_destino = 'Seccion 9 comprimido'
shutil.make_archive(archivo_destino, 'zip', carpeta_origen)


shutil.unpack_archive('Seccion 9 comprimido.zip','Extraccion', 'zip')