diccionario = {}
diccionario = {1: "Mito", 2: "Code", 3: "Jaime"}

print(diccionario)

diccionario[1] = "MitoCode"
print(diccionario)

print("El diccionario es de " + str(len(diccionario)) + " elementos")

print("Code" in diccionario)
print(2 in diccionario)

#del diccionario[1]
#print(diccionario)

print(diccionario.get(2))
print(diccionario.get(5))
print(diccionario.get(5, "No hay valor asociado"))

for k, v in diccionario.items():
    print("Llave " + str(k) + " Valor " + str(v))

print(diccionario.keys())
print(diccionario.values())

####################
valor = "Ninguno"

if valor == 1:
    print("Rojo") #funcionA
elif valor == 2:
    print("Azul") #funcionB
 elif valor == 3:
    print("Verde")

colores = {1: "Rojo", 2: "Azul", 3: "Verde"}
print(colores[1])
print(colores.get(1))






















