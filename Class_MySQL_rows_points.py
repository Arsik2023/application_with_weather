import pymysql

class MySQL_points:
    def __init__(self):
        pass
    def MySQL_points(self):
        connection = pymysql.connect(
                    host = '127.0.0.1',
                    port = 3306,
                    user = 'mysql',
                    password = 'mysql',

                    database = 'mtfirstdb',
                    cursorclass = pymysql.cursors.DictCursor # это область в памяти базы данных, которая предназначена для хранения последнего оператора SQL
                )
        with connection.cursor() as cursor:
            list_points = []
            query = "SELECT * FROM weather"
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                list_points.append(row['points'])
        return list_points
""" m = MySQL_points()
print(m.MySQL_points())     """