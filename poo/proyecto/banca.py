class Persona: 
    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona): 
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Datos del cliente:\n- Nombre completo: {self.nombre} {self.apellido}\n- Cuenta N°: {self.numero_cuenta}\n- Balance: {self.balance} "

    def depositar(self,deposito):
        if deposito < 0 : 
            print('No puedes ingresar una cantidad negativa')
        
        self.balance += deposito



    def retirar(self, retiro): 
        if retiro > self.balance: 
            print("No tienes ese dinero disponible") 
            return
        elif retiro < 0: 
            print('No puedes retirar un valor negativo')
            return
        self.balance -= retiro

def crear_cliente(): 
    nombre_cl = input("Ingrese su nombre: ")
    apellido_cl = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese su numero de cuenta: ")
    cliente = Cliente(nombre_cl, apellido_cl, numero_cuenta)
    return cliente

def inicio(): 
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0
    
    while opcion != 'S': 
        opcion = input('Elije: Depositar (D), Retirar (R), Salir (S): ')
        
        if opcion == "D": 
            monto_dep = int(input('Monton a depositar: '))
            mi_cliente.depositar(monto_dep)
        elif opcion == "R":
            monto_retirar = int(input("Monto a retirar")) 
            mi_cliente.retirar(monto_retirar)
        print(mi_cliente)
    
    print("Gracias por operar en Banco")

inicio()