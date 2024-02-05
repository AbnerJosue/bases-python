from pathlib import Path, PureWindowsPath

carpeta = Path('/Users/josue/Estudios/python') / 'otro_archivo.txt'
# mi_archivo = open(carpeta)
# print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)


# trasformar la ruta de windows

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)


ruta = Path('C:/Users/Usuario/Desktop/Curso Python') / 'Cuestionario Día 6' / 'Pregunta 1'
carpeta = ruta.parents[3]

print(carpeta)