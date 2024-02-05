def numero_perfumeria(): 
    for n in range(1, 10000):
        yield f"P - {n}"

def numero_enfermeria(): 
    for n in range(1, 10000):
        yield f"E - {n}"

def numero_cosmeticos(): 
    for n in range(1, 10000):
        yield f"C - {n}"


p = numero_enfermeria()
c = numero_cosmeticos()
e = numero_enfermeria()

def decorador(rubro): 
    print('\n'+ '*' * 23)
    print("Su numero es: ")
    if rubro == 'P': 
        print(next(p))
    elif rubro == 'E': 
        print(next(e))
    else: 
        print(next(c))

    print("Aguarge y sera atendido")
    print("*" * 23 + '\n' )
