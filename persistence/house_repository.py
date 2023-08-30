import sqlite3

from business_logic.model.house import House
from persistence.repository_base import RepositoryBase


class HouseRepository(RepositoryBase):

    def __init__(self, database_uri: str):
        super().__init__(database_uri)

    def list_houses(self) -> [House]:
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        sql = '''select ID, NAME, POINTS from houses'''
        cursor.execute(sql)

        houses: [House] = []
        for row in cursor:
            houses.append(House(*row))

        cursor.close()
        conn.close()

        return houses
