class Persona:

    codigo = 0

    def __init__(self, nombre):
        self.codigo = 5
        self.nombre = nombre

    def saludar(self):
        print("Hola " + self.nombre)


persona1 = Persona("Mito")
print(persona1.nombre)
print(persona1.codigo)

persona2 = Persona("Code")
print(persona2.nombre)
print(persona2.codigo)

persona3 = Persona("MitoCode")
persona3.saludar()