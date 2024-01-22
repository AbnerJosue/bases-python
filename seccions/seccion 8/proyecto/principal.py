import numeros


def preguntar(): 
    
    print("Bienvenidos a la farmacia Abner")

    while True: 
        print(" [P] - Perfumeria\n [E] - Enfermeria\n [C] - Cosmeticos")
        try: 
            rubro_seleccionado = input('Elija su rubro: ').upper()
            ["P", "E", "C"].index(rubro_seleccionado)   
        except ValueError: 
            print('El valor que selecciono no es correcto')
        else: 
            break
    numeros.decorador(rubro_seleccionado)

def inicio():
    while True: 
        preguntar()
        try: 
            turno = input('Desea otro turno? [Y] - [N]: ').upper()
            ['Y' , 'N'].index(turno)
        except ValueError:
            print('No se ha seleccionado un valor valido')
        else: 
            if turno == "N": 
                print('Gracias vuelva pronto')
                break

if __name__ == '__main__':
    inicio()
