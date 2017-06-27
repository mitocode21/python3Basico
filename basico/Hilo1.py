import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-s) %(message)s')


class Hilo1(threading.Thread):
    def __init__(self, nombre_hilo, id_persona, data):
        threading.Thread.__init__(self, name=nombre_hilo, target=Hilo1.consultar, args=(self, id_persona, ))
        # self.nombreHilo = nombre_hilo
        # self.id_persona = id_persona
        # self.data = data

    """def run(self):
        self.consultar(self.id_persona)"""

    def consultar(self, id_persona):
        logging.debug("Consultando para el id " + str(id_persona))
        time.sleep(2)
        return
