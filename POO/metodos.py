# metodos 
# def __init__ constructor

class Pajaro:
    se_volar = False
    def __init__(self,color, especie): # metodo constructor 
        self.color = color
        self.especie = especie
    
    def piar(self): # metodo constructor 
        print(f'PIO PIO PIO Mi color es {self.color}')
        print(f'Sabe volar ? {self.se_volar}')

    def volar(self,metros):
        print(f'El pajaro ha volado {metros}')

    
    def pintar_negro(self): 
        self.color = 'negro'
    # metodos de clase 
    @classmethod # no se puede acceder a los metodos de clase de instancia con self
    def poner_huevos(cls, cantidad_huevos): 
        print(f'Puso {cantidad_huevos}')
        cls.se_volar = False
    # tipos de metodos estaticos
    @staticmethod # funciona para que no modifiquen la instancica
    def mirar():
        print('El pajaro mira')


# atributos de instancia
mi_pajaro = Pajaro(color="green", especie='Tucan')
mi_pajaro.volar(10)
mi_pajaro.piar()

Pajaro.poner_huevos(20) # no se necesita una instancia para ejecutarse
Pajaro.mirar() 



