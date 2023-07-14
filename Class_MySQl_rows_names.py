import pymysql

class MySQL_names:
    def __init__(self):
        pass
    def MySQL_names(self):
        connection = pymysql.connect(
                    host = '127.0.0.1',
                    port = 3306,
                    user = 'mysql',
                    password = 'mysql',
                    database = 'mtfirstdb',
                    cursorclass = pymysql.cursors.DictCursor # это область в памяти базы данных, которая предназначена для хранения последнего оператора SQL
                )
        with connection.cursor() as cursor:
            list_names = []
            quety = "SELECT * FROM weather"
            cursor.execute(quety)
            rows = cursor.fetchall()
            for row in rows:
                list_names.append(row['name'])
        return list_names