import sqlite3

from business_logic.model.student import Student
from persistence.repository_base import RepositoryBase


class StudentRepository(RepositoryBase):

    def __init__(self, database_uri: str):
        super().__init__(database_uri)

    def list_students(self, first_name: str, last_name: str, house_id: int) -> [Student]:
        cursor = self.conn.cursor()

        first_name = '%' + first_name + '%'
        last_name = '%' + last_name + '%'

        sql = '''
        select ID, first_name, last_name, house_id from students
        where first_name like ? and last_name like ? and house_id=?'''

        cursor.execute(sql, [first_name, last_name, house_id])

        students: [Student] = []
        for row in cursor:
            students.append(Student(*row))

        cursor.close()

        return students
