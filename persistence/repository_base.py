import sqlite3


class RepositoryBase:
    def __init__(self, database_uri: str):
        self.conn = sqlite3.connect(database_uri)

    def __del__(self):
        self.conn.close()