import pymysql

class MySQL_update:
    def __init__(self, name_user, temperature_user, weather_user, speed_wind_user, time_user, points_user, index_user):
        self.name_user = name_user
        self.temperature_user = temperature_user
        self.weather_user = weather_user
        self.speed_wind_user = speed_wind_user
        self.time_user = time_user
        self.points_user = points_user
        self.index_user = index_user
    def update(self):
        connection = pymysql.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'mysql',
            password = 'mysql',
            database = 'mtfirstdb',
            cursorclass = pymysql.cursors.DictCursor # это область в памяти базы данных, которая предназначена для хранения последнего оператора SQL
        )
        with connection.cursor() as cursor:
            #! UPDATE weather SET name = "утюг", temperature = 12, weather="дождь", speed_wind=6, points=7 WHERE id = 100
            query = "UPDATE weather SET name = " + '"' + str(self.name_user) + '"' + ", temperature = " + str(self.temperature_user) + ", weather = " + '"' + str(self.weather_user) + '", speed_wind = ' + str(self.speed_wind_user) + ', data = "' + str(self.time_user) + '"' + ', points = ' + str(self.points_user) + " WHERE id = " + str(self.index_user) + ';'
            cursor.execute(query)
            connection.commit()
""" a = MySQL_update("Арс", 12, "дождь", 6, "время", 12, 112)
a.update() """