""" Модуль предназначен для запроса постов пользователя по 2-м тегам
"""

from model import Post, User, Tag, Session


def get_user_post(username, tags):
    """ Функция запрашивает посты 
    любого пользователя с конкретным тегом
    """
    session = Session()
    for tag in tags:
        print(session.query(Post).join(User).
              filter(User.username == username).
              filter(Tag.name == tag).all())


if __name__ == '__main__':
    username = input("Введите имя пользователя:")
    tag1, tag2 = input("Выберете два любых тега:").split()
    tags = [tag1, tag2]
    get_user_post(username, tags)
