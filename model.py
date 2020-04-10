""" Модуль описывает модели БД (или таблицы): User, Post, Tag
и включает функции добавления данных
"""

from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, scoped_session

Base = declarative_base()
engine = create_engine('sqlite:///blog_for_parents.db')  # создали подключение к базе
session_factory = sessionmaker(bind=engine)  # генерация фабрики сессий в это подключение
Session = scoped_session(session_factory)  # класс скопа сессий

# вспомогательная таблица:
tags_posts_table = Table('tags_posts', Base.metadata,
                         Column('post_id', Integer, ForeignKey('posts.id'), primary_key=True),
                         Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True))


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(16), nullable=False)

    posts = relationship("Post", back_populates="user")

    def __repr__(self):
        return f"{self.id} user: {self.username}"


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    title = Column(String(140), nullable=False)
    text = Column(Text, nullable=False)
    is_publised = Column(Boolean, default=False)

    user: User = relationship("User", back_populates="posts", lazy="joined")
    tags = relationship("Tag", secondary=tags_posts_table, back_populates="posts")

    def __repr__(self):
        return f"{self.id} post: {self.title}"


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    posts = relationship("Post", secondary=tags_posts_table, back_populates="tags")

    def __repr__(self):
        return f"Tag {self.id} – {self.name}"


def create_data():
    """ Функция добавляет данные в базу:
     – 2 пользователя
     – 4 поста (у каждого пользователя по 2 поста)
     – 3 тега
     """
    session = Session()
    user1 = User(username="Kate")
    user2 = User(username="Anna")
    user_list = (user1, user2)
    session.add_all(user_list)  # добавляем новых юзеров в сессию
    session.commit()

    post1 = Post(user_id=user1.id, title="Programming for kids in Minecraft",
                 text="MakeCode for Minecraft makes learning to code super fun...")
    post2 = Post(user_id=user1.id, title="Playing with python",
                 text="Online classes might be the most popular way for kids to"
                      "learn Python these days, and for good reason... ")
    post3 = Post(user_id=user2.id, title="Top 9 Kids Coding Languages of 2020",
                 text="In fact, programming for kids is becoming an increasingly popular topic...")
    post4 = Post(user_id=user2.id, title="Coding for Beginners: A Step-by-Step Guide for Kids, Parents, and Educators",
                 text="In this guide Coding for Beginners: A Step-by-Step Guide, "
                      "we are going to break down coding for kids into bite sized chunks... ")
    post_list = (post1, post2, post3, post4)
    session.add_all(post_list)

    session.commit()  # сохраняем изменения


def tags_add():
    """ Функция добавляет теги к постам, запрошенным из базы
     """
    session = Session()

    tag1 = Tag(name="python")
    tag2 = Tag(name="course")
    tag3 = Tag(name="minecraft")
    tag_list = (tag1, tag2, tag3)
    session.add_all(tag_list)  # добавляем теги в базу

    # вытягиваем теги из базы:
    tag1 = session.query(Tag)[0]
    tag2 = session.query(Tag)[1]
    tag3 = session.query(Tag)[2]

    # вытягиваем посты и добавляем для них теги:
    post1 = session.query(Post)[0]
    post1.tags.append(tag2)
    post1.tags.append(tag3)

    post2 = session.query(Post)[1]
    post2.tags.append(tag1)

    post3 = session.query(Post)[2]
    post3.tags.append(tag1)

    post4 = session.query(Post)[3]
    post4.tags.append(tag2)

    session.commit()


if __name__ == '__main__':
    # создаем таблицу
    Base.metadata.create_all(engine)
    # вызов функций добавления новых данных:
    create_data()
    tags_add()