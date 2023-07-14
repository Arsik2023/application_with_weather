import pymysql

class MySQL_login:
    def __init__(self):
        pass
    def MySQL_login(self):
        connection = pymysql.connect(
                    host = '127.0.0.1',
                    port = 3306,
                    user = 'mysql',
                    password = 'mysql',
                    database = 'mtfirstdb',
                    cursorclass = pymysql.cursors.DictCursor # это область в памяти базы данных, которая предназначена для хранения последнего оператора SQL
                )
        with connection.cursor() as cursor:
            list_logins = []
            quety = "SELECT * FROM weather"
            cursor.execute(quety)
            rows = cursor.fetchall()
            for row in rows:
                list_logins.append(row['login'])
        return list_logins
""" a = MySQL_login()
print(a.MySQL_login()) """