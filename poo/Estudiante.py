from .Persona import Persona
from .Docente import Docente


class Estudiante(Persona):

    def __init__(self):
        self.nombre = "Code"
        super().__init__(1, self.nombre, 26)

    def saludar(self):
        print("Hola mi nombre es " + self.nombre)

    def mostrar_edad(self, edad):
        print("Edad: " + edad)