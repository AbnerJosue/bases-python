class Pajaro:
    # atributos de clase 
    alas = True
                # el mismo : self 
    def __init__(self,color, especie): # metodo constructor 
        self.color = color
        self.especie = especie
# atributos de instancia
mi_pajaro = Pajaro(color="green", especie='Tucan')

print(mi_pajaro.especie)
print(mi_pajaro.alas)