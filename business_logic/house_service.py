from persistence.house_repository import HouseRepository
from config import config


class HouseService:

    def __init__(self):
        self.house_repo = HouseRepository(config.database) # TODO refactor this hidden dependency

    def list_houses(self):
        return self.house_repo.list_houses()
