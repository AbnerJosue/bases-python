class Persona: 
    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona): 
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Datos del cliente:\n- Nombre completo: {self.nombre} {self.apellido}\n- Cuenta N°: {self.numero_cuenta}\n- Balance: {self.balance} "

    def depositar(self):
        deposito = int(input('Cuanto dinero desea agregar a la cuenta:'))
        if deposito < 0 : 
            print('No puedes ingresar una cantidad negativa')
        
        self.balance += deposito



    def retirar(self): 
        retiro = int(input('Cuanto dinero desea retirar'))
        if retiro > self.balance: 
            print("No tienes ese dinero disponible") 
            return
        elif retiro < 0: 
            print('No puedes retirar un valor negativo')
            return
        self.balance -= retiro



elegir_opcion = ''
nombre_cliente = 'Abner'
apellido_cliente = 'Estrada'
balance = 0
numero_cuenta = '40239929993'

ejecutar_accion = Cliente(nombre_cliente,apellido_cliente,numero_cuenta,balance)


while elegir_opcion != '4':
    print("""Seleccione las opciones: 
        [1]: Depositar 
        [2]: Retirar
        [3]: Nombre de cuenta
        [4]: Salir
      """)
    elegir_opcion = input('Selecciona: ')

    if elegir_opcion == "1": 
        ejecutar_accion.depositar()
    elif elegir_opcion == "2": 
        ejecutar_accion.retirar()
    elif elegir_opcion == "3": 
        print(str(ejecutar_accion))