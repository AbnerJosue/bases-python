from random import shuffle

# Lista inicial 
palitos = ['-', '--','---', '----']


# funcion mezclar los palitos 
def mezclar(lista):
    shuffle(lista)
    return lista


# pedirle intento al usuario 
def probar_suerte():
    intento = ''

    while intento not in ['1','2','3','4']:
        intento = input('Elige un numero del 1 al 4: ')
    return int(intento)

# Comprobar el intento 

def chequear_intento(lista, intento):
    if lista[intento -1] == '-': 
        print("A lavar los platos")
    else: 
        print('Esta vez te has salvado')
    
    print(f'Te ha tocado {lista[intento-1]}')


chequear_intento(mezclar(palitos), probar_suerte())


from random import randint

def lanzar_dados(): 
    valor1 = randint(1,7)
    valor2 = randint(1,7)
    
    return (valor1,valor2)
    
valor1,valor2 = lanzar_dados()
def evaluar_jugada(valor1,valor2):
    suma_dados = valor1 + valor2
    
    if suma_dados == 6: 
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10: 
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else: 
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
    

lista_numeros = [1,2,15,7,2]

def reducir_lista(lista_numeros): 
    list_set = lista_numeros.sort()
    
    print(list_set)
        
reducir_lista(lista_numeros)

def valores (a,b,c): 
    print(a,b,c)

valores('2','3','4')