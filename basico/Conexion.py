import pymysql


class Conexion:

    def __init__(self, servidor, usuario, clave, base_datos):
        self.db = pymysql.connect(servidor, usuario, clave, base_datos)
        self.cursor = self.db.cursor()
        print("Conexión a Base de datos exitosa")

    def ejecutar_sentencia(self, sql):
        self.cursor.execute(sql)
        return self.cursor

    def cerrar_conexion(self):
        self.db.close()
        print("Base de datos desconectada")

    def commit(self):
        self.db.commit()
        return

    def rollback(self):
        self.db.rollback()
        return

