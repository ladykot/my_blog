##Цель: 

Создать модели Post, Tag для сайта "Мой блог" на любую тему. 
Для пользователя можно использовать стандартную модель User. 
Установить связи между моделями. Добавить некоторые данные. 
Выбрать все посты конкретного пользователя с 2-мя любыми тегами

##Установка:

Добавляем необходимые библиотеки:

    pip install -r requirements.txt
    
##Запуск:

Модели для пользователей, постов и тегов описаны в model.py. 
Чтобы добавить новые данные в базу, запускаем model.py:

    python model.py
    
##Запрос в базу данных:

Для полуения постов пошльзователя по тегам, запускаем main.py:

    python main.py
    




