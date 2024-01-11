# listas
my_list = ['a', 'b', 'c']
my_list2 = ['e','f']
conct_list = my_list + my_list2

conct_list[0] = 'alfa'
conct_list.append('valores')
eliminado = conct_list.pop(0)

print(conct_list)
print(len(conct_list))
print(eliminado)

lista = ['g','o','b']
lista.sort()
lista.reverse()
print(lista)

# Diccionario
diccionario = {
    'nombre': "Josue",
    'edad': 20
}

print(diccionario)

print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())

# Tuples

""" Los Tuples no se modifican y ocupan menos espacio en memoria , son inmutables """

my_tuple = (1,2,3,4)

print(type(my_tuple))

# my_tuple[0] = 2 # 'tuple' object does not support item assignment

t = (5, (10,20), 'values')

print(t[2][0])
print(list(t))
print(tuple(t))


t1 = (2,13,4,13)

x,y,z,c = t1

print(x,y,z)

print(t1.count(2)) # cantidad de veces que aparece ese numero
print(t1.index(13)) # indice que se encuentra ese numero


# Sets

my_set = set([1,2,3,4,5,7])

print(my_set)   

s1 = {1,3,4}
s2 = {23,4,5}
s1.add(209)
#s1.remove(3)
#s1.discard(1) # 1
#s1.pop()
s1.clear()
s3 = s1.union(s2)
print(s3)
print(s3)

palabra = "exito"

print(palabra[4])



