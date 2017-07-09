from basico.Conexion import Conexion

"""db = pymysql.connect('localhost', 'root', '123', 'test')
print(db)

cursor = db.cursor()
cursor.execute("SELECT VERSION()")
version = cursor.fetchone()
print(version)

sql = "INSERT INTO Persona(nombres, apellidos) values('Jaime', 'Medina')"
cursor.execute(sql)
db.commit()

sql = "SELECT id, nombres, apellidos FROM Persona"
cursor.execute(sql)
datos = cursor.fetchall()

for data in datos:
    print(data[0])
    print(data[1])
    print(data[2])

db.close()"""

try:
    cx = Conexion('localhost', 'root', '123', 'test')
    #sql = "INSERT INTO Persona(nombres, apellidos) values('Code', 'Code')"
    sql = "SELECT id, nombres, apellidos FROM Persona"
    cursor = cx.ejecutar_sentencia(sql)
    datos = cursor.fetchall()
    for data in datos:
        print(data[0])
        print(data[1])
        print(data[2])

    #cx.commit()
except Exception as e:
    cx.rollback()
    print(e)
finally:
    cx.cerrar_conexion()

