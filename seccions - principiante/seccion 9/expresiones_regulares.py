# EXPRESIONES REGULARES
import re 

texto = 'Si necesitas ayuda llama al (502) 32068534 servicio de ayuda '

patron = 'ayuda'

busqueda = re.findall(patron, texto)

for hallazgo in re.finditer(patron,texto): 
    print(hallazgo.span())


# texto = "LLama 502-3206-8534 ya mismo"

# patron = r'\d\d\d\-\d\d\d\d-\d\d\d\d'

# resultado = re.search(patron,texto)

# print(resultado)
    

texto = "LLama 502-3206-8534 ya mismo"
patron = r'\d{3}\-\d{4}\-\d{4}'
resultado = re.search(patron,texto)
print(resultado)


