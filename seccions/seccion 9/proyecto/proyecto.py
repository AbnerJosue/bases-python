import re 
import os 
import time
import datetime
from pathlib import Path
import math

ruta = 'C:\\Users\\josue\\Estudios\\python\\Python-Curso\\seccions\\seccion 9\\proyecto\\Mi_Gran_Directorio'

inicio = time.time()
patron = r'N\D{3}-\d{5}'
hoy = datetime.datetime.today()

nros_encontrados = []
archivos_encontrados = []

def buscar_numero(archivo, patron): 
    file_name = open(archivo, 'r')
    text = file_name.read()
    if re.search(patron, text):
        return re.search(patron, text)
    else: 
        return ''


def crear_lista():
    for carpeta, subcarpeta, archivo in os.walk(ruta): 
        for a in archivo: 
            result = buscar_numero(Path(carpeta, a), patron)
            if result != '':
                nros_encontrados.append((result.group()))
                archivos_encontrados.append(a.title())

def mostrar_todo():
    indice = 0
    print('-' * 50)
    print(f'Fecha de busqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('-------\t\t\t---------------')
    for a in archivos_encontrados: 
        print(f'{a}\t{nros_encontrados[indice]}')
        indice += 1
    print('\n')
    print(f'Numero encontrados: {len(nros_encontrados)}')
    print()
    fin = time.time()
    duracion = fin - inicio
    print(f'Duracion del programa: {math.ceil(duracion)}')
    print('-' * 50)


crear_lista()
mostrar_todo()
