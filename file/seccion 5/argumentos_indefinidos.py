# Argumentos Indefinidos (*args)
def suma(*args): 
    total = 0
    for arg in args: 
        total += arg

    return total

print(suma(2,4,5,62,34,2,24,6))


# Argumentos Indefinidos (*args)
def suma_facil(*args): 
    
    return sum(args)

print(suma_facil(2,4,5,62,34,2,24,6))