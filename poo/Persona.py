class Persona:

    def __init__(self, codigo, nombre, edad):
        self.codigo = codigo
        self._nombre = nombre
        self.__edad = edad

    def __saludar(self):
        print("Hola " + self.nombre)


persona1 = Persona(1, "Mito", 26)
print(persona1.codigo)
print(persona1._nombre)
print(persona1._Persona__edad)

persona1.nombre = "Code"
persona1._Persona__edad = 27
persona1._Persona__saludar()
print(persona1._Persona__edad)
