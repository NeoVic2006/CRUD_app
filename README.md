# CRUD_app приложение. 

**Установка:** 
Было использовано при создании: **PyQt5, Python 3.8, SQlite**.                      
Скопируйте депозит из репозитория: https://github.com/NeoVic2006/CRUD_app.git   

Установите все Dependences с посощью poetry файла poetry.lock: **poetry install**                       
Если у вас не установлен Poetry, то просто установите PyQt5: **pip install PyQt5**        
Запустите Mainwindow.py: **python Mainwindow.py**


**Функционал.** 
Приложение "Телефонная Книга". (Тестовый Админ аккаунт: Username: ser, Password: 123)

Запуск программы -> 
1) Окно верификациию(Логин с существуюим Аккаунтом, Регистрация нового аккаунта, Восстановление пароля) 
   Регистрация Нового аккаунта -> Нужно ввести Имя, пароль, подтверждение пароля и день рождения.
   Восстановление парол -> Нужно ввести Email. 
   Также функция "Show password" скрывает или показывает пароль при вводе. 

2) При успешной верификации пользователя открывается окно Пользователя где можно увидеть отсортированную БД по выбранному TAB значению.
   Также можно Добавлять, Удалять и Изменять выбранных пользователей. 
3) Также при входе нас встречает Сообщение Дня с информацией о пользователях у которых день рождения будет в следующие 7 дней. 

**Схема БД:**
   
![Image](https://user-images.githubusercontent.com/48185629/126081804-477f4caf-dc10-49d6-aaa4-00bd9b9e1cfd.PNG)


**Возможные улучшения:**

1) Уменьшить кол-во кода. Код в некоторых местах повторяетя, так что можно оптимизировать сделав еще пару функций. 
2) Выделить все функции работающие с БД в отдельный файл. 
3) Сделать функцию refresh. Чтобы каждый раз когда БД обновляется, автотически показывать результат. 
4) Сделать проверку Regular Expressions для всех вводных данных. Чтобы перед добавлением в БД проверять данные на правильность.
5) Улучшить naming для всех функций. Укоротить и переименовать. 
6) Удалять и обновлять Юзеров не по Имени и Телефону. а по ID. 
7) Я использовал Базу Данных SQlite, что усложнило создание Query запросов, так как, наример, в SQlite нет функции DATEDIFF.
8) Отсортировать файлы в Папки 


**Известные баги:**
https://github.com/NeoVic2006/CRUD_app/issues
