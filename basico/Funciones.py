# https://www.python.org/dev/peps/pep-0008/
"""def mi_funcion():
    return


def mi_funcion(param1):
    # codigo
    print(param1)
    return

mi_funcion("MitoCode")
mi_funcion(8)


def mi_funcion(param2, param1="Mito"):
    print(param1)
    print(param2)
    return

mi_funcion("Code")


def mi_funcion(param1, param2, *param_n):
    print(param1)
    print(param2)
    for x in param_n:
        print(x)
    return

mi_funcion(1, 2, 3, 4, 5, "Mito")


def mi_funcion(param1):
    return param1 * 2

print(mi_funcion(1))


texto = "Mito"


def mi_funcion():
    texto = "Code"
    return texto

print(texto)
print(mi_funcion())
"""
############################
"""Ejercicio
Realizar una función que permita hacer una conversión de divisas a dólares, tener en cuenta lo siguiente:
-De Soles a Dolares (valor cambio 3.256 PEN = 1 USD)
-De Pesos Méxicanos a Dolares(valor cambio 20 MXN = 1 USD)
-De no indicar un tipo de moneda inicial se debera asumir por defecto la moneda soles, 
-El usuario puede redefinir los valores de cambio de las divisas
-De no existir la divisa se deberá agregar considerando un valor de cambio ingresado por el usuario
retornar el monto convertido en dolares.
utilizar variables locales y globales necesarias"""


divisas = {"PEN": 3.256, "MXN": 20}


def definir_tipo_cambio(tipo_moneda, valor_cambio):
    divisas[tipo_moneda] = valor_cambio
    return


def convertir(monto_inicial, tipo_moneda="PEN"):
    valor = divisas.get(tipo_moneda)
    monto_final = monto_inicial / valor
    return monto_final


print("Ingrese la moneda y valor de cambio [separados por coma (,)")
texto = str(input()).split(",")
moneda = texto[0]
valor_cambio = float(texto[1])

definir_tipo_cambio(moneda, valor_cambio)
print("Ingrese el monto a convertir en " + moneda + " a USD")
monto = float(input())
resultado = convertir(monto, moneda)
print(str(monto) + " " + str(moneda) + " en USD es " + str(resultado))

