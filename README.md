# English version
## This project was not created for any global purposes, I wrote it for my own skills honing SQL and API queries, OOP(Object-orientir programming) and creating a graphical interface using the tkinter library
## The essence of the project
### It is a graphical interface in which there is registration and authorization, in which users try to guess the values of temperature, weather and wind speed (in m/s), I take them from the OpenWeather website. Then their bets on the weather and login with password are entered into the database during registration and at the same time, using the datetime library, the time is determined which is also entered into the database, this was done so that the user could not make a lot of bets at any time. Also, for correct predictions, the user will be awarded points and you can also see which user scored the maximum number of points
## Classes
* ### Class file Class_MySQL_connection.py it was made to enter the values of temperature, weather, wind speed, login, password, time at which the data was entered into the database and points
* ### Class file Class_MySQL_rows_login.py was made for user registration. Since during registration, the login could already have been created and in the future an error could occur in the database due to two identical logins
* ### Class file Class_MySQl_rows_names.py it was made so that all users have different names, since when the maximum points are deducted, there may be users with different names and it will not be clear who won
* ### Class file Class_update.py it was made to update the data in the database when re-betting on the weather. Updated time, user name, and his weather bets along with points
* ### In the class file Class_avtorisation_login_and_password.py there are 4 lists with login, password, user id in the database and the number of points
* ### In the class file Class_marks_data_base.py list of names who received the maximum score and the score itself
* ### In the class file Class_Requests.py a list consisting of temperature, weather and wind speed (in m/s) in the city of Yekaterinburg from the OpenWeather website
## The Final_interface.py file contains user authorization and registration and uses all the classes I listed above
## The only error I couldn't solve is that the code doesn't work on other computers when doing actions in the database
## I also converted this code into an application via PyInstaller (python library), you first need to download it (pip install pyinstaller) and go to the directory with the file Final_interface.py by entering the command python -m PyInstaller -w -F into the console Final_interface.py


---


# Версия на русском языке
## Этот проект не был создан для каких-либо глобальных целей, я его написал для своего оттачивания навыков SQL и API-запросов, ООП(Объектно-ориентированное программиование) и создания графического интерфейса с помощью библиотеки tkinter
## Суть проекта
### Он из себя представляет графический интерфейс, в котором есть регистрация и авторизация, в нём пользователи пытаются отгадать значения температуры, погоды и скорости ветра(в м/с), я их беру с сайта OpenWeather. Потом их ставки на погоду и логин с паролем при регистрации вносятся в базу данных и одновременно с помощью библиотеки datetime определяется время которое тоже заноситься в базу, это было сделанно для того, чтобы пользователь не мог в любой момент времени сделать много ставок. Также за правильные прогнозирования пользователю будут присваиваться очки и ещё можно посмотреть, какой пользователь набрал максимальное количество очков
## Классы
* ### Файл с классом Class_MySQL_connection.py был сделан для внесения значений температуры, погоды, скорости ветра, логина, пароля, времени, в котором произошло внесение данных в базу и очков
* ### Файл с классом Class_MySQL_rows_login.py был сделан для регистрации пользователя. Так как при регистрации логин уже мог быть создан и в дальнейшем могла возникнуть ошибка в базе данных из-за двух одинаковых логинов
* ### Файл с классом Class_MySQl_rows_names.py был сделан для того, чтобы у всех пользователей были разные имена, так как при выводе максимальных очков могут быть пользователи с разными именами и не будет понятно, кто выйграл
* ### Файл с классом Class_update.py был сделан для обновления данных в базе при повторной ставке на погоду. Обновляется время, имя пользователя, и его ставки на погоду вместе с очками
* ### В файле с классом Class_avtorisation_login_and_password.py есть 4 списка с логином, паролем, id пользователя в базе данных и количество очков
* ### В файле с классом Class_marks_data_base.py список имён, получивших максимальный балл и сам балл
* ### В файле с классом Class_Requests.py список, состоящий из температуры, погоды и скорости ветра(в м/с) в городе Екатеринбург с сайта OpenWeather
## Файл Final_interface.py содержит авторизацию и регистрацию пользователей и использует все классы, которые я перечислил выше
## Единственная ошибка, которую я не смог решить, это то, что код не работает на других компьютрах при действиях в базе данных
## Ещё я сконвертировал этот код в приложение через PyInstaller(библиотека на питоне), её предварительно нужно скачать(pip install pyinstaller) и перейти в дерикторию с файлом Final_interface.py, введя в консоль команду python -m PyInstaller -w -F Final_interface.py
