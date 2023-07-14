import pymysql

class MySQL:
    def __init__(self, name_user, temperature_user, weather_user, speed_wind_user, login_user, password_user, time_user, points_user):
        self.name_user = name_user
        self.temperature_user = temperature_user
        self.weather_user = weather_user
        self.speed_wind_user = speed_wind_user
        self.login_user = login_user
        self.password_user = password_user
        self.time_user = time_user
        self.points_user = points_user
    def connection(self):
        connection = pymysql.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'mysql',
            password = 'mysql',
            database = 'mtfirstdb',
            cursorclass = pymysql.cursors.DictCursor # это область в памяти базы данных, которая предназначена для хранения последнего оператора SQL
        )
        with connection.cursor() as cursor:
            query = "INSERT INTO weather (name, temperature, weather, speed_wind, login, password, data, points) VALUES (" + '"' + str(self.name_user) + '"' + ", " + str(self.temperature_user) + ", " + '"' + str(self.weather_user) + '"' + ", " + str(self.speed_wind_user) + ", " + '"' + str(self.login_user) + '"' + ", " + '"' + str(self.password_user) + '"' + ", " + '"' + str(self.time_user) + '"' + ', ' + str(self.points_user) + ");"
            cursor.execute(query)
            connection.commit()
        connection.close()
        
""" Vanya = MySQL('Арсен', 17, 'дождливо', 7, 'qwerty', 'vdfv', 'fgvfd', 0)
Vanya.connection() """