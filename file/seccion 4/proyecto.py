# proyecto

# - ANALIZADOR DE TEXTO 
# INGRESAR UN TEXTO UN PARRAFO ETC
# INGRESAR TRES LETRAS 
# -CUANTAS VECES LAS PALABRAS QUE ELIGIO (MAY, MINISCULAS) , PASAR EL TEXTO EN MINUSCULAS TODAS
# -CUANTAS PALABRAS HAY EN TODO EL TEXT
# -PRIMERA LETRA Y EL ULTIMO 
# - PALABRAS EN INVERSO 
# - APARECE PYTHON 

texto = input('Ingresa un texto a eleccion:')
letras = [ ]

texto = texto.lower()

letras.append(input('ingresa la primera palabra').lower())
letras.append(input('ingresa la segunta palabra').lower())
letras.append(input('ingresa la tercera palabra').lower())

print("\n")

print("CANTIDAD DE LETRAS")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2= texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f'Hemos encontrado la letra {letras[0]} repetida {cantidad_letras1} veces')
print(f'Hemos encontrado la letra {letras[1]} repetida {cantidad_letras2} veces')
print(f'Hemos encontrado la letra {letras[2]} repetida {cantidad_letras3} veces')
print(f'El total de palabras son {len(texto)}')
print(f'La primera palabra {texto.split()[0]}')
print(f'La ultima palabra {texto.split()[-1]}')
print(f'Palabra en inverso {texto[::-1]}')
