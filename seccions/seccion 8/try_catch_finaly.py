def suma():
    try: 
        n1 = int(input('Ingrese numero 1'))
        n2 = int(input('Ingrese numero 2'))

        print(n1 + n2)

    except TypeError: 
        # codigo a ejecutar si hay un error
        print("Estas intentando concatenar tipos distintos")
    except ValueError: 
        print("Estas intentado agregar un caracter y no un numero")
    else: 
        # codigo si no hay un error
        print("Hiciste todo bien") 

    finally: 
        # codigo que va ajecutar a todos modos
        print("Eso fue todo")

# suma()

def pedir_numero():
    while True: 
        try: 
            numero = int(input('Dame un numero'))
        except: 
            print('Ha ocurrido un error')

        else: 
            print(f'Ingresaste el numero {numero}')
            break
    print('Gracias')

pedir_numero()
            