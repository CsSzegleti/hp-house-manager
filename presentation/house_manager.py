from business_logic.house_service import HouseService


class HouseManager:

    def __init__(self):
        self.house_service = HouseService()

    def list_houses(self):
        houses = self.house_service.list_houses()

        for house in houses:
            print(house.name)

        input("Press ENTER to exit...")