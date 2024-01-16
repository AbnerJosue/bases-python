class Animal:
    def __init__(self, edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Ha nacido")

    def hablar(self): 
        print('HOLA')

# herencia de Animal 
class Pajaro(Animal): 
    # heredado y modificados
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad,color) # hereda la construccion
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print('ADIOS')
    
    def volar(self, metros): 
        print('El pajaro vuela {}'.format(metros))


piolin = Pajaro(2, 'Amarillo', 100)

piolin.hablar()
piolin.volar(200)


#//////////////////////////////////////
class Madre():
    def reir(self): 
        print('HOLA JAJJA')

class Padre(): 
    def hablar(self): 
        print("HOLA") 

class Hijo(Padre, Madre): 
    pass

class Nieto(Hijo):
    pass

hijo = Hijo()
nieto = Nieto()
nieto.hablar()

hijo.hablar()
hijo.reir()