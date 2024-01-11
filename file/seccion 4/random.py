from random import (
    randint,
    uniform,
    random, 
    choice, 
    shuffle
)

aleatorio = randint(1,50)
print(aleatorio)


uniform_aleatorio = uniform(1,5)

print(uniform_aleatorio)

aleatorio_round = round(uniform(1,5),2)

print(aleatorio_round)

aleatorio_random = random()
print(aleatorio_random)

colores = ['azul', 'rojo', 'verde']

aleatorio_color = choice(colores)

numeros = list(range(5,100,5))

aleatorio_numero = shuffle(numeros)

# compresion de listas 

palabra = 'python'

lista = []

for letra in palabra: 
    lista.append(letra)

print(lista)

lista2 = [ letra for letra in palabra]

print(lista2)

lista3 = [n  if n * 2 > 10 else 'no' for n in range(0,21,2)]
