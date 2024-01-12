# solo lectura 
# lectura = open('prueba.txt', 'r')
# print(lectura.read())
# lectura.close()
# solo escritura 

# escritura elimina lo que ya esta y agrega lo nuevo
escritura = open('prueba.txt', 'w')
escritura.writelines(['soy el nuevo texto', 'HOLA MUNDO', 'AQUI ESTOY'])
escritura.close()

# write debajo de lo existente 
# agregar = open('prueba.txt', 'a')
# agregar.write('HOLA MUNDO COMO ESTAS')
