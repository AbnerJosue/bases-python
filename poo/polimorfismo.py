# polimorfismo 
# muchas formas 
# objetos con diferentes formas

class Vaca: 
    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + 'dice muu')

class Oveja: 
    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + 'dice bee')


vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')


# animales = [vaca1, oveja1]

# for animal in animales:
#     animal.hablar()

def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)
animal_habla(oveja1)


class Mago:
    def atacar(self):
        print("Ataque mágico")

class Arquero:
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai:
    def atacar(self):
        print("Ataque con katana")
        

arquero_1 = Arquero()
mago_1 = Mago()
samurai_1 = Samurai()

personajes = [arquero_1,mago_1,samurai_1]

for personaje in personajes: 
    personaje.atacar()
    
