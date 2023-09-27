import sqlite3

from business_logic.model.house import House
from persistence.repository_base import RepositoryBase


class HouseRepository(RepositoryBase):

    def __init__(self, database_uri: str):
        super().__init__(database_uri)

    def list_houses(self) -> [House]:
        cursor = self.conn.cursor()
        sql = '''
        select ID, NAME, POINTS from houses'''
        cursor.execute(sql)

        houses: [House] = []
        for row in cursor:
            houses.append(House(*row))

        cursor.close()

        return houses

    def get_house_by_id(self, obj_id: int):
        cursor = self.conn.cursor()
        sql = '''
        select ID, NAME, POINTS from houses where ID=?'''
        cursor.execute(sql, [obj_id])

        if cursor.arraysize == 0:
            raise Exception("error.entity.not.found")

        house: House = House(*cursor)

        cursor.close()

        return house

    def add_score(self, obj_id: int, score:int ):
        cursors = self.conn.cursor()
        sql = '''
        update houses
        set POINTS = POINTS +?
        where ID = ?'''
        cursors.execute(sql,[score,obj_id])
        cursors.close()
