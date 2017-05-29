def funcion1():
    try:
        5/0
    except ZeroDivisionError:
        print("Division no permitida")
    return


def funcion2():
    try:
        open("/home/mitocode/no_file.txt","r")
    except IOError:
        print("No existe archivo")
    return


def funcion3():
    archivo = None
    try:
        # 5/0
        archivo = open("/home/mitocode/no_file.txt", "r")
        # float("MitoCode")
    except ZeroDivisionError:
        print("División no válida")
    except (IOError, ValueError):
        print("Lectura/Escritura Error")
    except ValueError:
        print("Tipo dato no válido")
    except Exception:
        print("Excepción general")
    finally:
        if archivo is not None:
            archivo.close()
    return


def funcion4():
    try:
        # open("/home/mitocode/no_file.txt", "r")
        raise ValueError("No se encuentra el tipo de dato")
        raise Exception("Error general")
    except ValueError as ex:
        # print(ex)
        raise
    except Exception as ex:
        print(ex)
    return


# funcion1()
# funcion2()
# funcion3()
funcion4()