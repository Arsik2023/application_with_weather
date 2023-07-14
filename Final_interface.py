from tkinter import *
from Class_MySQL_rows_login import * #! Класс со строками логина в бд
from Class_MySQl_rows_names import * #! Класс со строками имени в бд
from Class_Requests import * #! Класс с прогнозами погоды
from Class_MySQL_connection import * #! Класс внесения данных пользователя в базу
from Class_marks_data_base import * #! Класс с максимальным баллом и пользователей с ним
from Class_avtorisation_login_and_password import * #! Класс с id, логином и паролем
from Class_MySQL_update import * #! Класс для обновления данных
import datetime as dt #! Служит для времени

#! Для цветных коментов я использовал расширение Colorful Comments
window = Tk()
#! Функция после того, как пользователь нажмёт регистрацию
def after_button_registration():
    #! Все кнопки удаляются
    button_registration.destroy()
    button_avtorisation.destroy()
    #! Строка ругания пользователя на логин
    string_login_mat = Label(window, text='', font=(font, size))
    string_login_mat.place(x=900, y=120)
    #! Строка ругания пользователя на пароль
    string_password_mat = Label(window, text='', font=(font, size))
    string_password_mat.place(x=900, y=150)
    #! Строка, что чел регистрацию выбрал
    string_title_registration = Label(window, text='Регистрация', font=(font, 25))
    string_title_registration.place(x=500, y=50)
    #! Строка для логина
    string_login = Label(window, text='Введите логин:', font=(font, size))
    string_login.place(x=400, y=120)
    #! Вводимое окно для логина
    entry_login = Entry(window, width=50)
    entry_login.place(x=565, y=130)
    #! Строка для пароля
    string_password = Label(window, text='Введите пароль:', font=(font, size))
    string_password.place(x=400, y=150)
    #! Вводимое окно для пароля
    entry_password = Entry(window, width=50)
    entry_password.place(x=575, y=160)
    #! Строка ругания пользователя на логин
    string_login_mat = Label(window, text='', font=(font, size))
    string_login_mat.place(x=900, y=120)
    #! Строка ругания пользователя на пароль
    string_password_mat = Label(window, text='', font=(font, size))
    string_password_mat.place(x=900, y=150)
    #! Функция для проверки данных в регистрации
    def check_registration():
        #! Ввод логина в переменную
        res_login = entry_login.get()
        #! Ввод пароля в переменную
        res_password = entry_password.get()
        #! Булевые значения, которые принимают истину, если логин и паролль удовлетворяет критериям
        bool_login = 0
        bool_password = 0
        #! Вводимое логина в переменную
        res_login = entry_login.get()
        #! Вводимое пароля в переменную
        res_password = entry_password.get()
        #! Список логинов в базе
        list_logins_in_base = MySQL_login()
        list_logins_in_base = list_logins_in_base.MySQL_login()
        #! Проверка на длину логина
        if len(res_login) == 0:
            string_login_mat.configure(text='Поле заполнение логина не должно быть пустым')
            bool_login = 0
        elif len(res_login) > 15:
            string_login_mat.configure(text='Логин не должен быть больше 15 символов')
            bool_login = 0
        else:
            string_login_mat.configure(text='Ваш логин: ' + str(res_login))
            bool_login = 1
        #! Проверка на длину пароля
        if len(res_password) == 0:
            string_password_mat.configure(text='Поле заполнение пароля не должно быть пустым')
            bool_password = 0
        elif len(res_password) > 15:
            string_password_mat.configure(text='Пароль не должен быть больше 15 символов')
            bool_password = 0
        else:
            string_password_mat.configure(text='Ваш пароль: ' + str(res_password))
            bool_password = 1
        #! Проверка, есть ли логин в базе
        if str(res_login) in list_logins_in_base:
            string_login_mat.configure(text='Такой логин занят, введите другой')
            bool_login = 0
        #! Функция для чистки окна, когда пользователь закончит регистрацию
        def finish_registration():
            button_registration.destroy()
            string_login_mat.destroy()
            string_password_mat.destroy()
            string_title_registration.destroy()
            string_login.destroy()
            entry_login.destroy()
            string_password.destroy()
            entry_password.destroy()
            button_start_registration.destroy()
            #! Уже появился логин и пароль в этой функции
            def check_rates_and_name():
                #! Значение окон в переменных
                res_name = name_entry.get()
                res_temperature = temperature_entry.get()
                res_speed_wind = speed_wind_entry.get()
                res_weather = weather_entry.get() 
                #! Проверка данных
                #! Проверка имени
                if len(res_name) == 0:
                    string_name_data.configure(text='Нельзя оставлять поле заполнения имени пустым')
                    unit_name = 0
                elif len(res_name) > 15:
                    string_name_data.configure(text='Нельзя вводить имя больше 15 символов, введите ещё раз')
                    unit_name = 0  
                else:
                    string_name_data.configure(text='Имя пользователя: '+res_name)
                    unit_name = 1
                #! Список имён в базе
                list_names_in_data_base = MySQL_names()
                list_names_in_data_base = list_names_in_data_base.MySQL_names()
                #! Проверка имён в базе данных
                if res_name in list_names_in_data_base:
                    string_name_data.configure(text='Такое имя занято, введите другое')
                    unit_name = 0
                #! Проверка температуры
                if len(res_temperature) == 0:
                    string_temperature_data.configure(text='Нельзя оставлять поле заполнения температуры пустым')
                    unit_temperature = 0
                elif res_temperature[0] == '-':
                    if res_temperature.lstrip('-').isdigit():
                        if len(res_temperature) >= 4:
                            string_temperature_data.configure(text='Такая температура быть не может')
                            unit_temperature = 0
                        else:
                            string_temperature_data.configure(text='Ставка на температуру: '+res_temperature)
                            unit_temperature = 1
                    else:
                        string_temperature_data.configure(text='Температура является числом')
                        unit_temperature = 0
                else:
                    if res_temperature.isdigit():
                        if len(res_temperature) >= 3:
                            string_temperature_data.configure(text='Такая температура быть не может')
                            unit_temperature = 0
                        else:
                            string_temperature_data.configure(text='Ставка на температуру: '+res_temperature)
                            unit_temperature = 1
                    else:
                        string_temperature_data.configure(text='Температура является числом')
                        unit_temperature = 0
                #! Проверка ветра
                if len(res_speed_wind) == 0:
                    string_speed_wind_data.configure(text='Нельзя оставлять поле заполнения скорости ветра пустым')
                    unit_speed_wind = 0
                elif res_speed_wind[0] == '-':
                    if res_speed_wind.lstrip('-').isdigit():
                        string_speed_wind_data.configure(text='Такая скорость ветра быть не может')
                        unit_speed_wind = 0
                    else:
                        string_speed_wind_data.configure(text='Скорость ветра является числом')
                        unit_speed_wind = 0
                else:
                    if res_speed_wind.isdigit():
                        if len(res_speed_wind) >= 3:
                            string_speed_wind_data.configure(text='Такая скорость ветра быть не может')
                            unit_speed_wind = 0
                        else:
                            string_speed_wind_data.configure(text='Ставка на скорость ветра: '+res_speed_wind)
                            unit_speed_wind = 1
                    else:
                        string_speed_wind_data.configure(text='Скорость ветра является числом')
                        unit_speed_wind = 0
                #! Проверка погоды
                if len(res_weather) == 0:
                    string_weather_data.configure(text='Нельзя оставлять поле заполнения погоды пустым')
                    unit_weather = 0
                elif len(res_weather) > 40:
                    string_weather_data.configure(text='Нельзя вводить погоду больше 40 символов, введите ещё раз')
                    unit_weather = 0
                else:
                    string_weather_data.configure(text='Ставка на погоду: '+res_weather)
                    unit_weather = 1
                #! Проверка на наличие всех удовлетворённых потребностей
                unit_all = unit_name * unit_temperature * unit_speed_wind * unit_weather
                #! Провека правильных ответов, если пользователь ввёл данные правильно
                if unit_all == 1:
                    points = 0
                    # Лист из ответов на погоду
                    list_datas = Requests()
                    list_datas = list_datas.Requests()
                    # Проверка на правильные ответы и добавление очков
                    if int(res_temperature) == list_datas[0]:
                        points = points + 1
                    if int(res_speed_wind) == list_datas[1]:
                        points = points + 1
                    if str(res_weather) == list_datas[2]:
                        points = points + 3
                    #! Время UTC
                    utc_time = dt.datetime.utcnow()
                    #! Накидываем время до Екб
                    period = dt.timedelta(hours=5)
                    #! Определяем время в Екб
                    ekb_time = utc_time + period
                    #! Нужно прибавить 6 часов
                    ekb_time = ekb_time + dt.timedelta(hours=6)
                    #! Конвертируем в строку
                    ekb_time = str(ekb_time)
                    #! Внесения данных пользователя в бд
                    MySQL(res_name, res_temperature, res_weather, res_speed_wind, res_login, res_password, ekb_time, points).connection()
                    #! Говорим, что всё чётко
                    string_succes_data_base = Label(window, text='Ваше имя и ставки были успешно добавлены в базу данных', font=(font, size))
                    string_succes_data_base.place(x=0, y=240)
                    string_succes_six_hour = Label(window, text='Вы можете ввести следующую ставку через 6 часов', font=(font, size))
                    string_succes_six_hour.place(x=0, y=270)
                    string_succes_data_base_see = Label(window, text='Вы можете посмотреть у каких пользователей наибольшее количество очков', font=(font, size))
                    string_succes_data_base_see.place(x=0, y=300)
                    #! Функция для просмотра наибольших очков
                    def see_max_point():
                        #! Удаляем всё
                        name_entry.destroy()
                        temperature_entry.destroy()
                        speed_wind_entry.destroy()
                        weather_entry.destroy()
                        string_name_data.destroy()
                        string_temperature_data.destroy()
                        string_speed_wind_data.destroy()
                        string_weather_data.destroy()
                        string_name.destroy()
                        string_temperature.destroy()
                        string_speed_wind.destroy()
                        string_weather.destroy()
                        string_succes_data_base.destroy()
                        string_succes_six_hour.destroy()
                        string_succes_data_base_see.destroy()
                        string_print_datas.destroy()
                        first_string.destroy()
                        second_string.destroy()
                        #! Теперь сделаю список с максимальным баллом и его обладателей
                        list_max_points_and_user = Marks_data_base()
                        list_max_points_and_user = list_max_points_and_user.Marks_data_base()
                        #! Поймём какой максимальный балл
                        max_point = list_max_points_and_user[-1]
                        #! Разделение на количество пользователей
                        if len(list_max_points_and_user) > 2:
                            list_max_points_and_user.remove(max_point)
                            string_users_max_points = ", ".join(list_max_points_and_user)
                            #! Делаем строку с максимальным баллом и пользователями
                            text_string = 'Максимальный бал, равный ' + str(max_point) + ', получили пользователи: ' + string_users_max_points
                            string_max_point_and_users = Label(window, text=text_string, font=(font, size))
                            string_max_point_and_users.place(x=0, y=0)
                        else:
                            text_string = 'Максимальный бал, равный ' + str(max_point) + ', получил пользователь ' + list_max_points_and_user[0]
                            string_max_point_and_users = Label(window, text=text_string, font=(font, size))
                            string_max_point_and_users.place(x=0, y=0)
                        #! Функция для всего уничтожения
                        def destroy_all():
                            window.destroy()
                        button_destroy_all = Button(window, text='Выйти', font=(font, size), command=destroy_all)
                        button_destroy_all.place(x=0, y=30)
                    
                    button_max_point = Button(window, text='Посмотреть', font=(font, size), command = lambda: [see_max_point(), button_max_point.destroy()])
                    button_max_point.place(x=0, y=330)
            #! Кнопка для вывода данных
            string_print_datas = Button(window, text='Сохранить данные в базу', font=(font, size), command=check_rates_and_name)
            string_print_datas.place(x=0, y=190)
            #! Строки для данных
            #! Строка имени
            string_name_data = Label(window, text='', font=(font, size))
            string_name_data.place(x=800, y=50)
            #! Строка температуры
            string_temperature_data = Label(window, text='', font=(font, size))
            string_temperature_data.place(x=800, y=80)
            #! Строка ветра
            string_speed_wind_data = Label(window, text='', font=(font, size))
            string_speed_wind_data.place(x=800, y=110)
            #! Строка погоды
            string_weather_data = Label(window, text='', font=(font, size))
            string_weather_data.place(x=800, y=140)
            #! Первая строка
            first_string = Label(window, text='Добро пожаловать на платформу "Ставки на погоду"', font=(font, size))
            first_string.place(x=0, y=0)
            second_string = Label(window, text='Для начала вам нужно ввести ваши прогнозы на погоду и имя', font=(font, size))
            second_string.place(x=0, y=30)
            #! Строка имени
            string_name = Label(window, text='Введите ваше имя:', font=(font, size))
            string_name.place(x=0, y=60)
            name_entry = Entry(window, width=50)
            name_entry.place(x=200, y=67)
            #! Строка температууры
            string_temperature = Label(window, text='Введите прогноз на температуру:', font=(font, size))
            string_temperature.place(x=0, y=90)
            temperature_entry = Entry(window, width=50)
            temperature_entry.place(x=360, y=99)
            #! Строка ветра
            string_speed_wind = Label(window, text='Введите прогноз на скорость ветра в м/с:', font=(font, size))
            string_speed_wind.place(x=0, y=120)
            speed_wind_entry = Entry(window, width=50)
            speed_wind_entry.place(x=450, y=129)
            #! Строка погоды
            string_weather = Label(window, text='Введите прогноз на погоду:', font=(font, size))
            string_weather.place(x=0, y=150)
            weather_entry = Entry(window, width=50)
            weather_entry.place(x=300, y=160)
        if bool_login * bool_password == 1:
            #! Кнопка, что регистрация закончилась
            button_finish_registration = Button(window, text='Закончить регистрацию', font=(font, size), command=lambda: [finish_registration(), button_finish_registration.destroy()])
            button_finish_registration.place(x=610, y=200)
    #! Кнопка, что регистрация началась
    button_start_registration = Button(window, text='Сохранить данные', font=(font, size), command=check_registration)
    button_start_registration.place(x=400, y=200)
    
def after_button_avtorisation():
    #! Все кнопки удаляются
    button_registration.destroy()
    button_avtorisation.destroy()
    #! Строка ругания пользователя на логин
    string_login_mat = Label(window, text='', font=(font, size))
    string_login_mat.place(x=900, y=120)
    #! Строка ругания пользователя на пароль
    string_password_mat = Label(window, text='', font=(font, size))
    string_password_mat.place(x=900, y=150)
    #! Строка, что чел авторизацию выбрал
    string_title_avtorisation = Label(window, text='Авторизация', font=(font, 25))
    string_title_avtorisation.place(x=500, y=50)
    #! Строка для логина
    string_login = Label(window, text='Введите логин:', font=(font, size))
    string_login.place(x=400, y=120)
    #! Вводимое окно для логина
    entry_login = Entry(window, width=50)
    entry_login.place(x=565, y=130)
    #! Строка для пароля
    string_password = Label(window, text='Введите пароль:', font=(font, size))
    string_password.place(x=400, y=150)
    #! Вводимое окно для пароля
    entry_password = Entry(window, width=50)
    entry_password.place(x=575, y=160)
    #! Строка ругания пользователя на логин
    string_login_mat = Label(window, text='', font=(font, size))
    string_login_mat.place(x=900, y=120)
    #! Строка ругания пользователя на пароль
    string_password_mat = Label(window, text='', font=(font, size))
    string_password_mat.place(x=900, y=150)
    #! Функция для проверки логина и пароля
    def check_login_and_password():
        #! Делаем лист с логином и паролем
        list_logins_and_passwords = Avtorisation_login_and_password
        list_logins_and_passwords = list_logins_and_passwords.Avtorisation_login_and_password()
        #! Делаем лист с логимном
        list_login_in_db = list_logins_and_passwords[1]
        #! Делаем лист с паролем
        list_password_in_db = list_logins_and_passwords[2]
        #! Делаем лист с индексами
        list_id_in_db = list_logins_and_passwords[0]
        #! Делаем лист со временем
        list_time_in_db = list_logins_and_passwords[3]
        #! Делаем лист с очками
        list_point_in_db = list_logins_and_passwords[4]
        #! Ввод логина в переменную
        res_login = entry_login.get()
        #! Ввод пароля в переменную
        res_password = entry_password.get()
        #! Булевые значения, которые принимают истину, если логин и паролль удовлетворяет критериям
        bool_login = 0
        bool_password = 0
        #! Вводимое логина в переменную
        res_login = entry_login.get()
        #! Вводимое пароля в переменную
        res_password = entry_password.get()
        #! Проверка логина
        if res_login in list_login_in_db:
            index_login = list_login_in_db.index(res_login)
            string_login_mat.configure(text='Ваш логин: ' + str(res_login))
            if res_password in list_password_in_db:
                index_password = list_password_in_db.index(res_password)
                if index_login == index_password:
                    #! Какое время у пользователя
                    data_user_then = list_time_in_db[list_password_in_db.index(res_password)]
                    data_user_then = dt.datetime.strptime(data_user_then, '%Y-%m-%d %H:%M:%S.%f')
                    #! Время UTC
                    utc_time = dt.datetime.utcnow()
                    #! Накидываем время до Екб
                    period = dt.timedelta(hours=5)
                    #! Определяем время в Екб
                    ekb_time = utc_time + period
                    if ekb_time >= data_user_then:
                        string_password_mat.configure(text='Ваш пароль правильный')
                        button_finish_avtorisation = Button(window, text='Войти', font=(font, size), command=lambda: [after_finish_registration(), button_finish_avtorisation.destroy()])
                        button_finish_avtorisation.place(x=620, y=200)
                    else:
                        string_login_mat.configure(text='Вам нужно подождать до ' + str(data_user_then))
                        string_password_mat.configure(text='чтобы ещё раз сделать ставку')
                else:
                    string_password_mat.configure(text='Ваш пароль неправильный')
            else:
                string_password_mat.configure(text='Ваш пароль неправильный')
            
        else:
            string_login_mat.configure(text='Такого логина нет')
        #! Функция, что авторизация закончилась
        def after_finish_registration():
            string_password_mat.destroy()
            string_login_mat.destroy()
            string_login.destroy()
            string_password.destroy()
            string_title_avtorisation.destroy()
            entry_login.destroy()
            entry_password.destroy()
            button_avtorisation_check.destroy()
            def check_rates_and_name():
                #! Значение окон в переменных
                res_name = name_entry.get()
                res_temperature = temperature_entry.get()
                res_speed_wind = speed_wind_entry.get()
                res_weather = weather_entry.get() 
                #! Проверка данных
                #! Проверка имени
                if len(res_name) == 0:
                    string_name_data.configure(text='Нельзя оставлять поле заполнения имени пустым')
                    unit_name = 0
                elif len(res_name) > 15:
                    string_name_data.configure(text='Нельзя вводить имя больше 15 символов, введите ещё раз')
                    unit_name = 0  
                else:
                    string_name_data.configure(text='Имя пользователя: '+res_name)
                    unit_name = 1
                #! Список имён в базе
                list_names_in_data_base = MySQL_names()
                list_names_in_data_base = list_names_in_data_base.MySQL_names()
                #! Проверка имён в базе данных
                if res_name in list_names_in_data_base:
                    string_name_data.configure(text='Такое имя занято, введите другое')
                    unit_name = 0
                #! Проверка температуры
                if len(res_temperature) == 0:
                    string_temperature_data.configure(text='Нельзя оставлять поле заполнения температуры пустым')
                    unit_temperature = 0
                elif res_temperature[0] == '-':
                    if res_temperature.lstrip('-').isdigit():
                        if len(res_temperature) >= 4:
                            string_temperature_data.configure(text='Такая температура быть не может')
                            unit_temperature = 0
                        else:
                            string_temperature_data.configure(text='Ставка на температуру: '+res_temperature)
                            unit_temperature = 1
                    else:
                        string_temperature_data.configure(text='Температура является числом')
                        unit_temperature = 0
                else:
                    if res_temperature.isdigit():
                        if len(res_temperature) >= 3:
                            string_temperature_data.configure(text='Такая температура быть не может')
                            unit_temperature = 0
                        else:
                            string_temperature_data.configure(text='Ставка на температуру: '+res_temperature)
                            unit_temperature = 1
                    else:
                        string_temperature_data.configure(text='Температура является числом')
                        unit_temperature = 0
                #! Проверка ветра
                if len(res_speed_wind) == 0:
                    string_speed_wind_data.configure(text='Нельзя оставлять поле заполнения скорости ветра пустым')
                    unit_speed_wind = 0
                elif res_speed_wind[0] == '-':
                    if res_speed_wind.lstrip('-').isdigit():
                        string_speed_wind_data.configure(text='Такая скорость ветра быть не может')
                        unit_speed_wind = 0
                    else:
                        string_speed_wind_data.configure(text='Скорость ветра является числом')
                        unit_speed_wind = 0
                else:
                    if res_speed_wind.isdigit():
                        if len(res_speed_wind) >= 3:
                            string_speed_wind_data.configure(text='Такая скорость ветра быть не может')
                            unit_speed_wind = 0
                        else:
                            string_speed_wind_data.configure(text='Ставка на скорость ветра: '+res_speed_wind)
                            unit_speed_wind = 1
                    else:
                        string_speed_wind_data.configure(text='Скорость ветра является числом')
                        unit_speed_wind = 0
                #! Проверка погоды
                if len(res_weather) == 0:
                    string_weather_data.configure(text='Нельзя оставлять поле заполнения погоды пустым')
                    unit_weather = 0
                elif len(res_weather) > 40:
                    string_weather_data.configure(text='Нельзя вводить погоду больше 40 символов, введите ещё раз')
                    unit_weather = 0
                else:
                    string_weather_data.configure(text='Ставка на погоду: '+res_weather)
                    unit_weather = 1
                #! Проверка на наличие всех удовлетворённых потребностей
                unit_all = unit_name * unit_temperature * unit_speed_wind * unit_weather
                
                #! Провека правильных ответов, если пользователь ввёл данные правильно
                if unit_all == 1:
                    points = 0
                    # Лист из ответов на погоду
                    list_datas = Requests()
                    list_datas = list_datas.Requests()
                    # Проверка на правильные ответы и добавление очков
                    if int(res_temperature) == list_datas[0]:
                        points = points + 1
                    if int(res_speed_wind) == list_datas[1]:
                        points = points + 1
                    if str(res_weather) == list_datas[2]:
                        points = points + 3
                    #! Определяем какое сейчас время
                    #! Время UTC
                    utc_time = dt.datetime.utcnow()
                    #! Накидываем время до Екб
                    period = dt.timedelta(hours=5)
                    #! Определяем время в Екб
                    ekb_time = utc_time + period
                    #! Нужно прибавить 6 часов
                    ekb_time = ekb_time + dt.timedelta(hours=6)
                    #! Конвертируем в строку
                    ekb_time = str(ekb_time)
                    points = list_point_in_db[index_login] + points
                    index_user = list_id_in_db[index_login]
                    MySQL_update(res_name, res_temperature, res_weather, res_speed_wind, ekb_time, points, index_user).update()
                    #! Говорим, что всё чётко
                    string_succes_data_base = Label(window, text='Ваше имя и ставки были успешно добавлены в базу данных', font=(font, size))
                    string_succes_data_base.place(x=0, y=240)
                    string_succes_six_hour = Label(window, text='Вы можете ввести следующую ставку через 6 часов', font=(font, size))
                    string_succes_six_hour.place(x=0, y=270)
                    string_succes_data_base_see = Label(window, text='Вы можете посмотреть у каких пользователей наибольшее количество очков', font=(font, size))
                    string_succes_data_base_see.place(x=0, y=300)
                    button_max_point = Button(window, text='Посмотреть', font=(font, size), command = lambda: [see_max_point(), button_max_point.destroy()])
                    button_max_point.place(x=0, y=330)
                    #! Функция для просмотра наибольших очков
                    def see_max_point():
                        #! Удаляем всё
                        string_points_then.destroy()
                        name_entry.destroy()
                        temperature_entry.destroy()
                        speed_wind_entry.destroy()
                        weather_entry.destroy()
                        string_name_data.destroy()
                        string_temperature_data.destroy()
                        string_speed_wind_data.destroy()
                        string_weather_data.destroy()
                        string_name.destroy()
                        string_temperature.destroy()
                        string_speed_wind.destroy()
                        string_weather.destroy()
                        string_succes_data_base.destroy()
                        string_succes_six_hour.destroy()
                        string_succes_data_base_see.destroy()
                        string_print_datas.destroy()
                        first_string.destroy()
                        second_string.destroy()
                        #! Теперь сделаю список с максимальным баллом и его обладателей
                        list_max_points_and_user = Marks_data_base()
                        list_max_points_and_user = list_max_points_and_user.Marks_data_base()
                        #! Поймём какой максимальный балл
                        max_point = list_max_points_and_user[-1]
                        #! Разделение на количество пользователей
                        if len(list_max_points_and_user) > 2:
                            list_max_points_and_user.remove(max_point)
                            string_users_max_points = ", ".join(list_max_points_and_user)
                            #! Делаем строку с максимальным баллом и пользователями
                            text_string = 'Максимальный бал, равный ' + str(max_point) + ', получили пользователи: ' + string_users_max_points
                            string_max_point_and_users = Label(window, text=text_string, font=(font, size))
                            string_max_point_and_users.place(x=0, y=0)
                        else:
                            text_string = 'Максимальный бал, равный ' + str(max_point) + ', получил пользователь ' + list_max_points_and_user[0]
                            string_max_point_and_users = Label(window, text=text_string, font=(font, size))
                            string_max_point_and_users.place(x=0, y=0)
                        def destroy_all():
                            window.destroy()
                        button_destroy_all = Button(window, text='Выйти', font=(font, size), command=destroy_all)
                        button_destroy_all.place(x=0, y=30)
                        
                    
            #! Кнопка для вывода данных
            string_print_datas = Button(window, text='Сохранить данные в базу', font=(font, size), command=check_rates_and_name)
            string_print_datas.place(x=0, y=190)
            #! Строки для данных
            #! Строка имени
            string_name_data = Label(window, text='', font=(font, size))
            string_name_data.place(x=800, y=50)
            #! Строка температуры
            string_temperature_data = Label(window, text='', font=(font, size))
            string_temperature_data.place(x=800, y=80)
            #! Строка ветра
            string_speed_wind_data = Label(window, text='', font=(font, size))
            string_speed_wind_data.place(x=800, y=110)
            #! Строка погоды
            string_weather_data = Label(window, text='', font=(font, size))
            string_weather_data.place(x=800, y=140)
            #! Первая строка
            first_string = Label(window, text='Добро пожаловать на платформу "Ставки на погоду"', font=(font, size))
            first_string.place(x=0, y=0)
            second_string = Label(window, text='Для начала вам нужно ввести ваши прогнозы на погоду и имя', font=(font, size))
            second_string.place(x=0, y=30)
            #! Строка для очков пользователя 
            points_then = list_point_in_db[index_login]
            string_points_then = Label(window, text='Количество ваших очков: ' + str(points_then), font=(font, size))
            string_points_then.place(x=800, y=170)
            #! Строка имени
            string_name = Label(window, text='Введите ваше имя:', font=(font, size))
            string_name.place(x=0, y=60)
            name_entry = Entry(window, width=50)
            name_entry.place(x=200, y=67)
            #! Строка температууры
            string_temperature = Label(window, text='Введите прогноз на температуру:', font=(font, size))
            string_temperature.place(x=0, y=90)
            temperature_entry = Entry(window, width=50)
            temperature_entry.place(x=360, y=99)
            #! Строка ветра
            string_speed_wind = Label(window, text='Введите прогноз на скорость ветра в м/с:', font=(font, size))
            string_speed_wind.place(x=0, y=120)
            speed_wind_entry = Entry(window, width=50)
            speed_wind_entry.place(x=450, y=129)
            #! Строка погоды
            string_weather = Label(window, text='Введите прогноз на погоду:', font=(font, size))
            string_weather.place(x=0, y=150)
            weather_entry = Entry(window, width=50)
            weather_entry.place(x=300, y=160)
    
    #! Кнопка для авторизации пользователя
    button_avtorisation_check = Button(window, text='Сохранить данные', font=(font, size), command=check_login_and_password)
    button_avtorisation_check.place(x=400, y=200)
    

#! Шрифт и размеры текста
font = 'MV Boli'
size = 15
#! Разрешение монитора
width_px = window.winfo_screenwidth()
height_px = window.winfo_screenheight()
window.geometry(str(width_px)+'x'+str(height_px))
#! Титул окна
window.title('Горячий привет!')
#! функция после того, как нажали кнопку регистрации
#! Кнопка для регистрации
button_registration = Button(window, text='Регистрация', font=(font, size), command=after_button_registration)
button_registration.place(x=450, y=300)
#! Кнопка для авторизации
button_avtorisation = Button(window, text='Авторизация', font=(font, size), command=after_button_avtorisation)
button_avtorisation.place(x=600, y=300)
window.mainloop()