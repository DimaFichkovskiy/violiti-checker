import sqlalchemy as db
import psycopg2
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from data.config import SQLALCHEMY_DATABASE_URI


engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True, future=True)
Base = declarative_base(bind=engine)


class Users(Base):
    __tablename__ = 'users'

    id = db.Column(db.BIGINT(), primary_key=True)
    username = db.Column(db.String())
    full_name = db.Column(db.String())
    lots = relationship('Lots', backref='user', lazy='dynamic')


class Lots(Base):
    __tablename__ = 'lots'

    id = db.Column(db.Integer(), primary_key=True)
    link = db.Column(db.String())
    end_date = db.Column(db.DateTime())
    user_id = db.Column(db.BIGINT(), db.ForeignKey('users.id'))


class DBDriver:
    @classmethod
    def user_existence_check(cls, user_id):
        return cls.get_user(user_id) is None

    @classmethod
    def add_new_user(cls, user_id, username, full_name):
        with engine.connect() as conn:
            conn.execute(
                text("INSERT INTO users(id, username, full_name) VALUES (:id, :username, :full_name) RETURNING id"),
                [{"id": user_id, "username": username, "full_name": full_name}]
            )
            conn.commit()

    @classmethod
    def get_user(cls, user_id):
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM Users WHERE id=:id"),
                                  [{"id": user_id}])
            data = list(map(dict, result))
            return data[0] if data else None

    @classmethod
    def lot_existence_check(cls, link):
        return cls.get_lot(link) is None

    @classmethod
    def get_lot(cls, link):
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM Lots WHERE link=:link"),
                                  [{"link": link}])
            data = list(map(dict, result))
            return data[0] if data else None

    @classmethod
    def add_new_lot(cls, user_id, link, end_date):
        with engine.connect() as conn:
            conn.execute(
                text("INSERT INTO lots(link, user_id, end_date) VALUES (:link, :user_id, :end_date) RETURNING id"),
                [{"link": link, "user_id": user_id, "end_date": end_date}]
            )
            conn.commit()

    @classmethod
    def get_all_lots(cls, user_id):
        with engine.connect() as conn:
            result = conn.execute(
                text("SELECT * FROM Lots WHERE user_id=:user_id"),
                [{"user_id": user_id}]
            )
            print(result)
            data = list(map(dict, result))
            return data


if __name__ == '__main__':
    Base.metadata.create_all(engine)
