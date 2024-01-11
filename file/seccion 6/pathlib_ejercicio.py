from pathlib import Path, PureWindowsPath

carpeta = Path('/Users/josue/Estudios/python') / 'otro_archivo.txt'
# mi_archivo = open(carpeta)
# print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)


# trasformar la ruta de windows

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)