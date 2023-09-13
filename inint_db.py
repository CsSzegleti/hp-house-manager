import sqlite3
import config


def init_db():
    connection = sqlite3.connect(config.database)
    cursor = connection.cursor()
    with open ("persistence/database/init.sql","r") as sql_file:
        sql_script = sql_file.read()
    cursor.executescript(sql_script)
    cursor.close()
    connection.close()