# import math
# import sys
#from TipoCambio import convertir, definir_tipo_cambio
#import TipoCambioIn as tip
import importlib.machinery
import hola
from hola2 import saludar
# print(sys.path)


loader = importlib.machinery.SourceFileLoader('TipoCambioIn', '/home/mitocode/Programación/Python/python3Basico/basico/TipoCambioIn.py')
tip = loader.load_module('TipoCambioIn')

"""x = 55.62
print(math.floor(x))
print(math.ceil(x))

lista = [5.5, 5.2, 4, 3]

suma = sum(lista)
print(suma)

x = 256.89
resultado = math.trunc(x)
print(resultado)

resultado = math.pow(5, 2)
print(resultado)"""

"""print("Ingrese la moneda y valor de cambio [separados por coma (,)")
texto = str(input()).split(",")
moneda = texto[0]
valor_cambio = float(texto[1])

tip.definir_tipo_cambio(moneda, valor_cambio)
print("Ingrese el monto a convertir en " + moneda + " a USD")
monto = float(input())
resultado = tip.convertir(monto, moneda)
print(str(monto) + " " + str(moneda) + " en USD es " + str(resultado))"""

hola.saludar()
saludar()