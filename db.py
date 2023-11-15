import sqlite3 as sql
from classes import User
from config import config as cfg


class Database(object):
    def __init__(self, path_db: str):
        self.connection = sql.connect(path_db)
        self.cur = self.connection.cursor()

    def export_user(self, user: User):
        """
        обновляет данные о пользователе в БД
        :param user:
        :return:
        """
        pass

    def import_user(self, **kwargs):
        """
        создаёт один или несколько объектов User по данным из БД
        :param kwargs:
        :return:
        """
        pass

    def create_user(self, **kwargs):
        """
        Создаёт User и после экспортирует его в БД
        :param kwargs:
        :return:
        """
        pass
