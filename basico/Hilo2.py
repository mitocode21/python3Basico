import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-s) %(message)s')


class Hilo2(threading.Thread):
    def __init__(self, nombre_hilo, id_persona, data):
        threading.Thread.__init__(self, name=nombre_hilo, target=Hilo2.guardar, args=(self, id_persona, data))
        # self.nombreHilo = nombre_hilo
        # self.id_persona = id_persona
        # self.data = data

    """def run(self):
        self.guardar(self.id_persona, self.data)"""

    def guardar(self, id_persona, data):
        logging.info("Guardando para el id " + str(id_persona) + " la data " + data)
        time.sleep(5)
        return
