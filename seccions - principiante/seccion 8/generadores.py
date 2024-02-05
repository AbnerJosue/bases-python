"""
Generadores
"""

def mi_funcion(): 
    lista = []
    for x in range(4,10):
        lista.append(x*10)
    return lista

def mi_generador():
    for x in range(4,10):
        yield x * 10


print(mi_funcion())
print(mi_generador())

g = mi_generador()
print(next(g))
print(next(g))


