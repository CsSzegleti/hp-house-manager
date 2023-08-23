import sqlite3

from config import config


class HouseRepository:
    def list_houses(self):
        conn = sqlite3.connect("database/" + config.database)
        cursor = conn.cursor()
        sql = '''select ID, NAME, POINTS from houses'''
        cursor.execute(sql)



        cursor.close()
        conn.close()