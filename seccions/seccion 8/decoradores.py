"""
 funcion
"""

def cambiar_letras(tipo):
    def mayuscula(texto): 
        print(texto.upper())

    def minuscula(texto): 
        print(texto.lower())

    if tipo == "may": 
        return mayuscula
    elif tipo == "min": 
        return minuscula



operacion = cambiar_letras('may')

operacion('palabra')


"""
decorador
"""

def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('Adios')

    return otra_funcion

@decorar_saludo
def mayuscula(texto): 
    print(texto.upper())

@decorar_saludo
def minuscula(texto): 
    print(texto.lower())

minuscula('PALABRA')