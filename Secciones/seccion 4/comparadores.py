mi_bool = 10 == 24

print(mi_bool)

listas = ['a','b','c']

for letra in listas: 
    numero_letra = listas.index(letra) + 1 # obtener el index
    print(f'letra {numero_letra}: {letra}')

listas2 = ['pablo', 'laura', 'luis','josue']

for item in listas2: 
    if item.startswith('l'): 
        print(item)


for a,b in [[1,3], [2,4],[5,4]]:
    print(a)
    print(b)

dic = {'clave1': 'a', 'clave2': 'b'}

for item in dic.values():
    print(item)
for item in dic.items():
    print(item)
for item in dic:
    print(item)

# while 
    
monedas = 5

while monedas > 0: 
    print(f'tengo {monedas}')
    monedas -= 1
else: 
    print('No tengo mas dinero')

respuesta = input('')
while respuesta == 's':
    respuesta =  input('quieres seguir')
else: 
    print('Gracias')

while respuesta == 'n':
    pass


nombre = input('Tu nombre')
for letra in nombre:
    if letra == 'r': 
        break 
    print(letra)

nombre = input('Tu nombre')
for letra in nombre:
    if letra == 'r': 
        continue 
    print(letra)
