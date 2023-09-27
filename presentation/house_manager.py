from business_logic.house_service import HouseService
from presentation.menu import Menu


class HouseManager:

    def __init__(self):
        self.house_service = HouseService()

    def list_houses(self):
        houses = self.house_service.list_houses()
        house_menu = Menu("House list")

        for house in houses:
            house_menu.add_menu_item(str(house.name) + " " + str(house.points), self.list_house_students, house.id)

        house_menu.add_menu_item("Exit to house manager", house_menu.deactivate)
        house_menu.activate()

    def list_house_students(self, house_id):
        students = self.house_service.list_house_students(house_id)

        for student in students:
            print(f"{student.first_name} {student.last_name}")

        input("Press ENTER to exit...")
