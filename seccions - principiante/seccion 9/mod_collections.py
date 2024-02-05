from collections import Counter, defaultdict, namedtuple

numeros = [8,6,5,4,4,5,6,4,3,4,2,3,4]

# muestra cuantas veces esta repetido en un diccionario
print(Counter(numeros))
frase = 'al pan pan y al vino vino'
print(Counter(frase.split()))

serie = Counter([1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,4])
print(serie.most_common())
print(serie.elements())


# diccionario por defecto

from collections import defaultdict

# Crear un defaultdict con el valor predeterminado "Valor no hallado"
mi_diccionario = defaultdict(lambda: "Valor no hallado")

# Agregar el par de datos al diccionario
mi_diccionario['edad'] = 44

# Acceder a una clave existente
print(mi_diccionario['edad'])  # Salida: 44


# tupla con nombre
Persona = namedtuple('Persona', ['nombre','altura', 'peso'])
ariel = Persona('Ariel','10', '10kg')
print(ariel.altura)
mi_tupla = (500,19,54)

