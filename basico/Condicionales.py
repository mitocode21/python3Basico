#switch con diccionarios
#https://nideaderedes.urlansoft.com/2013/03/04/no-hay-switch-en-python/

#edad = 18
print("¿Cuál es tu edad?")
edad = int(input())

if edad > 18:
    mensaje = "Es mayor de edad"
elif edad < 0:
    mensaje = "Edad no valida"
else:
    mensaje = "Es menor de edad"

print(mensaje)
