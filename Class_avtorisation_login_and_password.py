import pymysql

class Avtorisation_login_and_password:
    def __init__(self):
        pass
    def Avtorisation_login_and_password():
        connection = pymysql.connect(
            host = '127.0.0.1',
                    port = 3306,
                    user = 'mysql',
                    password = 'mysql',
                    database = 'mtfirstdb',
                    cursorclass = pymysql.cursors.DictCursor # это область в памяти базы данных, которая предназначена для хранения последнего оператора SQL
        )
        with connection.cursor() as cursor:
            list_id = []
            list_logins = []
            list_passwords = []
            list_times = []
            list_points = []
            query = "SELECT * FROM weather"
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                list_id.append(row['id'])
                list_logins.append(row['login'])
                list_passwords.append(row['password'])
                list_times.append(row['data'])
                list_points.append(row['points'])
        return [list_id, list_logins, list_passwords, list_times, list_points]