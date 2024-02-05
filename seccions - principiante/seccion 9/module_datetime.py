from datetime import datetime , time, date

mi_hora = time(17, 35, 20)
mi_dia = date(2023,12,2)
print(mi_hora)
print(mi_dia)

nacimiento = date(1995,3,5)
defuncion = date(2095,6,18)

vida = defuncion - nacimiento
print(vida)

despierta = datetime(2022,10,5,7,30)
duerme = datetime(2022,10,5,23,45)

vigilia = duerme - despierta

hoy = date.today()
print(hoy)

minuto = datetime.now()
print(minuto.minute)