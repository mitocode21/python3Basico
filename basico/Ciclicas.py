for i in range(0, 5):  # range(2, 5):
    print("Iteración N° " + str(i))

for x in range(3):
    print("Iteración N° " + str(x))
    if x == 1:
        print("Se corto la interación N° " + str(x))
        break

for x in range(3):
    if x == 1:
        continue
    print("Iteración N° " + str(x))

for x in "Mit0C0de":
    if x.isdigit():
        print("Es número")
    print(x, end="\n")

for x in range(3):
    print("Iteración N° " + str(x))
    if x == 1:
        print("Entro al if")
        # break el else: solo se ejecuta luego de la ejecucion del for, el break no permite el else
else:
    print("Luego de la iteración N° " + str(x))

contador = 0
# while True:
while 1 == 1: #!=
    print("Iteración N° " + str(contador))
    # contador++
    contador += 1
    # break

contador = 0
while not contador < 5:
    print("Es menor a 5")
    contador += 1
    if contador == 3:
        print("En la iteracion")
        #break
else:
    print("Fin de la iteracion")

