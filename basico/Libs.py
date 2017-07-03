import pymysql

db = pymysql.connect('localhost', 'root', '123', 'test')
print(db)