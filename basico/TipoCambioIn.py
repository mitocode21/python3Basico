divisas = {"PEN": 3.256, "MXN": 20}


def definir_tipo_cambio(tipo_moneda, valor_cambio):
    divisas[tipo_moneda] = valor_cambio
    return


def convertir(monto_inicial, tipo_moneda="PEN"):
    valor = divisas.get(tipo_moneda)
    monto_final = monto_inicial / valor
    return monto_final

