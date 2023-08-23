from business_logic.model.hogwarts import Hogwarts
import random

from business_logic.model.house import House


class Student:
    def __init__(self, obj_id: int, first_name: str, last_name: str):
        self.id = obj_id
        self.first_name = first_name
        self.last_name = last_name
        self.house: House | None = None

    def assign_house(self, hogwarts: Hogwarts):
        house_idx = random.randint(0, 3)
        if self.house is not None:
            self.house.students.remove(self)

        self.house = hogwarts.houses[house_idx]
        hogwarts.houses[house_idx].students.append(self)

    def add_house_points(self, num_points: int) -> None:
        self.house.points += num_points

    def remove_house_points(self, num_points: int) -> None:
        new_points = self.house.points - num_points
        max(0, new_points)
