"""lista1 = ["Mito", "Code"]
lista2 = [1, 2, 3]
lista3 = ["Mito", "Code", 2]
lista4 = []
lista5 = list()

for x in lista1:
    print(x)

lista1.append("Jaime")
print(lista1)
lista1.append(["Mito", "Code"])
print(lista1)
lista1.extend(["Mito", "Code"])
print(lista1)
print(lista1[-1])
lista1[0] = "ABC"
print(lista1)
lista1[0:2] = ["Mito", "Peru"]
print(lista1)

for x in reversed(lista1):
    print(x)

print(list(reversed(lista1)))
texto = "Mito,Code,Jaime,Peru,Mito,Mito"
lista1 = texto.split(",")
print(lista1)

lista1.remove("Mito")
lista1 = [x for x in lista1 if x != "Mito"]
print(lista1)"""

########################################

#Se desea registrar las ventas de galletas del día de una tienda
#Jaime, 3
#Mito, 7
#Code, 5
#El cajero introduce mal el nombre del primer cliente y debe corregirlo
#Se desea conocer los nombres de los clientes
#Se desea imprimir en pantalla la suma de galletas
#Se debe registrar un cliente adicional que compre N galletas
#Imprimir las más recientes ventas

ventas = list()
for x in range(0, 3):
    print("Ingrese el nombre de la persona y la cantidad de galletas vendidas")
    entrada = str(input())
    cliente = entrada.split(",")
    ventas.append(cliente)

#ventas = [["Jaimt", 3], ["Mito", 7], ["Code", 5]]
#ventas[0] = ["Jaime", 3]

suma = 0
for cliente in ventas:
    suma += int(cliente[1])
    print("Cliente: " + cliente[0])
print("La cantidad de galletas vendidas fueron " + str(suma))

ventas.append(["MitoCode", 10])
print(ventas)
print(list(reversed(ventas)))
























































