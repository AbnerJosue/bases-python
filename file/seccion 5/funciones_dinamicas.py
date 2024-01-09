# funciones dinamicas 
# mas complejas

def chequear_3_cifras_ (lista):

    lista_3_cifras = [] 

    for n in lista: 
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else: 
            pass
    return lista_3_cifras

resultado_ = chequear_3_cifras_([ values for values in range(99,620,6)])

print(resultado_)


def chequear_3_cifras (numero):
    return numero in range(100,1000)

resultado = chequear_3_cifras(658)
print(resultado)

def todos_positivos(lista):
    for n in lista:
        if n <= 0:
            return False  # Si encuentra un número no positivo, devuelve False
    return True  # Solo llega aquí si todos los números son positivos


lista_numeros = [valores for valores in range(-20, 20)]


resultado = todos_positivos(lista_numeros)
print(resultado)


def cantidad_pares(lista):
    cuenta_pares = sum(1 for num in lista if num % 2 == 0)
    return cuenta_pares

# Ejemplo de lista con valores:
lista_numeros = [valores for valores in range(1, 11)]

# La función se invocaría de la siguiente manera:
resultado = cantidad_pares(lista_numeros)
print(resultado)

precios_cafe  = [('capuchino',1.5), ('Expreso', 1.2),('Moka', 1.9)]


def cafe_mas_caro(lista_precios):

    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe,precio in lista_precios: 
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else: 
            pass

    return (cafe_mas_caro, precio_mayor)

print(cafe_mas_caro(precios_cafe))