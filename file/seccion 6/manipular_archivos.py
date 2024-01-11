mi_archivo = open('prueba.txt')

# print(mi_archivo.read())
print(mi_archivo.readline().rstrip())
print(mi_archivo.readline()) # quitar salto de linea

mi_archivo.close()