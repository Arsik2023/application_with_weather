from Class_MySQl_rows_names import *
from Class_MySQL_rows_points import *

class Marks_data_base:
    def __init__(self):
        pass
    def Marks_data_base(self):
        #! Список всех имён в базе
        list_names = MySQL_names()
        list_names = list_names.MySQL_names()
        #! Спискок очков имён в базе
        list_points = MySQL_points()
        list_points = list_points.MySQL_points()
        #! Находим максимальную оценку
        max_point = max(list_points)
        #! Теперь мне нужен лист имён, получивших максимальный балл
        list_names_have_max_marks = []
        for i in range(len(list_points)):
            if list_points[i] == max_point:
                list_names_have_max_marks.append(list_names[i])
        list_names_have_max_marks.append(max_point)
        return list_names_have_max_marks
""" a = Marks_data_base()
print(a.Marks_data_base()) """