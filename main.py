""" Модуль, предназначенный для подключения к базе, 
создания сессии, добавления новых данных и их дальнейших изменений, 
добавления тегов и сохранения изменений в базе.
"""


from model import create_data, tags_add
from model import Base, Post, User, Tag, engine, Session


def get_user_post(username, tagname):
    """ Функция запрашивает посты 
    любого пользователя с конкретным тегом
    """
    session = Session()
    print(session.query(Post).join(User).filter(User.username == username).filter(Tag.name == tagname).all())


if __name__ == '__main__':
    # создаем таблицу
    Base.metadata.create_all(engine)
    # вызов функций добавления новых данных:
    create_data()
    tags_add()
    username = input("Имя пользователя:")
    tagname = input("Тег поста:")
    # вызов функции запроса постов пользователя
    get_user_post(username, tagname)
