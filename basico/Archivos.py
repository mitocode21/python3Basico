from shutil import copyfile

"""ruta = '/home/mitocode/Programación/Python/python3Basico/basico/txt/lenguajes.txt'
archivo = open(ruta, 'r')

# print(archivo.read())
# print(archivo.readline())
print(archivo.readlines())

archivo.close()"""

""""contenido = "C#,PHP,C,C++,TypeScript"
nueva_ruta = "/home/mitocode/Programación/Python/python3Basico/basico/txt/lenguajes_2.txt"
archivo = open(nueva_ruta, 'r+')  # w : write r : read
archivo.write(contenido)
archivo.seek(0)
# print(archivo.read())
for linea in archivo.readlines():
    print(linea)

archivo.close()"""

# copyfile("/home/mitocode/Programación/Python/python3Basico/basico/txt/lenguajes.txt","/home/mitocode/Programación/Python/python3Basico/basico/txt/lenguajes_3.txt")


def establecer_archivo(ruta, permiso):
    archivo = open(ruta, permiso)
    return archivo


def leer_archivo(archivo):
    contenido = archivo.read()
    return contenido


def escribir_archivo(archivo, texto):
    archivo.write('\n' + texto)


arch = establecer_archivo("/home/mitocode/Programación/Python/python3Basico/basico/txt/lenguajes.txt", "r+")
print(leer_archivo(arch))
escribir_archivo(arch, "MitoCode Pyhton")
arch.seek(0)
print(leer_archivo(arch))