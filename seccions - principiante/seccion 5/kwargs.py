def suma(**kwargs): 
    # print(type(kwargs))
    total = 0

    for key, valor in kwargs.items(): 
        print(key,valor)
        total += valor
    return total

suma(x=3, y=4,z=2)

def suma_(num1, num2, *args,**kwargs): 
    print(f'el primer valor es {num1}')
    print(f'el segundo valor es {num2}')

    for arg in args: 
        print(f'los args {arg}')

    for clave, valor in kwargs.items(): 
        print(f'{clave} = {valor}')

args = [123,123,322,334,444]
kwargs = {"x":10,"y":20,"m":20,"w":'valores'}
suma_(14,52, *args, **kwargs)