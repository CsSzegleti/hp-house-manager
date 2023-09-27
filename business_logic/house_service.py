from persistence.house_repository import HouseRepository
import config
from persistence.student_repository import StudentRepository


class HouseService:

    def __init__(self):
        self.house_repo = HouseRepository(config.database)  # TODO refactor this hidden dependency
        self.student_repo = StudentRepository(config.database)  # TODO refactor this hidden dependency

    def list_houses(self):
        return self.house_repo.list_houses()

    def list_house_students(self, house_id):
        return self.student_repo.list_students("", "", house_id)

    def add_points(self, house_id, points):
        self.house_repo.add_score(house_id, points)

    def take_points(self, house_id, points):
        self.house_repo.add_score(house_id, -1 * points)
