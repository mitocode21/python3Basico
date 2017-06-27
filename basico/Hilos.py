import threading
import time
import datetime
import logging
from basico.Hilo1 import Hilo1
from basico.Hilo2 import Hilo2

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-s) %(message)s')


def consultar(id_persona):
    logging.debug("Consultando para el id " + str(id_persona))
    time.sleep(2)
    return


def guardar(id_persona, data):
    logging.info("Guardando para el id " + str(id_persona) + " la data " + data)
    time.sleep(5)
    return

tiempo_ini = datetime.datetime.now()

# t1 = threading.Thread(name="hilo_1", target=consultar, args=(1, ))
# t2 = threading.Thread(name="hilo_2", target=guardar, args=(1, "¡Suscribete al canal Coder!"))

t1 = Hilo1("Hilo_1", 1, "")
t2 = Hilo2("Hilo_2", 1, "¡Suscribete al canal Coder!")

t1.start()
t2.start()
# consultar(1)
# guardar(1, "¡Suscribete al canal Coder!")

t1.join()
t2.join()

tiempo_fin = datetime.datetime.now()

print("Tiempo transcurrido " + str(tiempo_fin.second - tiempo_ini.second))
