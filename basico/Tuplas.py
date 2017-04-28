tupla = ()
print(tupla)

tupla = 1, 2, 3
print(tupla)

tupla = (1, 2, 3)
print(tupla)

tupla = (1, )
print(tupla)

tupla = (1, "MitoCode", True, ["Mito", "Code"])
print(tupla)

#tupla[2] = False
tupla[3][1] = "Codes"
print(tupla)

x, y, z, w = tupla
print(x)
print(y)
print(z)
print(w)

print(tupla[3])
print(tupla[-2])
print(tupla[1:3])
print(tupla[:3])

tupla1 = ("a", "b", "c")
tupla2 = ("d", "a", "f")

tupla3 = tupla1 + tupla2
print(tupla3)

tupla3 = tupla1 * 5
print(tupla3)

print(tupla3.count("a"))
print(tupla3.index("a"))

for x in tupla3:
    print(x)









































tupla1 = ("a", "b", "c")