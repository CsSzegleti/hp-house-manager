from business_logic.model.spell import Spell
from persistence.repository_base import RepositoryBase


class SpellRepository(RepositoryBase):
    def __init__(self, database_uri: str):
        super().__init__(database_uri)

    def list_spells(self):
        cursor = self.conn.cursor()
        sql = '''
        select ID, NAME, complexity, damage, min_level, description from spells'''
        cursor.execute(sql)

        spells: [Spell] = []
        for row in cursor:
            spells.append(Spell(*row))

        cursor.close()

        return spells
