import time
import datetime

print(time.time())
print(time.strftime("%H:%M:%S"))
print(time.strftime("%I:%M:%S"))
print(time.strftime("%d/%m/%y"))
print(time.strftime("%d/%m/%Y"))

tiempo = time.strftime("%H:%M:%S")
print(tiempo)

#%c: Fecha y Hora
#%x: Fecha
#%X: Hora
formato = "%X"
ahora = time.strftime(formato)
print(ahora)

print("--------------------")

ahora = datetime.datetime.now()
print(ahora)
print(ahora.minute)
print(ahora.month)
print(ahora.year)
print(datetime.date.today().year)

fecha = "21011991" #string
fecha = datetime.datetime.strptime(fecha, "%d%m%Y") #variable tipo fecha
print(fecha)

fecha = fecha - datetime.timedelta(days=3, weeks=1, hours=1)
print(fecha)


































