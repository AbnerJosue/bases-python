# ingresar nombre 
from random import (
    randint,
)

nombre = input('Ingresa tu nombre: ')

print(f"Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")

aleatorio = randint(1,100)

counter = 8

while counter != 0 : 
    numero = int(input('Ingrese el numero a buscar: '))
    counter -=1

    if numero < 0 or numero > 100: 
        print('El numero no es permitido: ')

    if  numero < aleatorio: 
        print(f'El numero es mayor te quedan {counter} intentos')

    elif numero > aleatorio: 
        print(f'El numero es menor te quedan {counter} intentos')
    else: 
        print(f'Has ganado el numero aletorio es {aleatorio} con {counter} intentos') 
        break

if numero != aleatorio: 
      print(f"Lo siento, se han agotado los intentos. El numero secreto era {aleatorio}")


