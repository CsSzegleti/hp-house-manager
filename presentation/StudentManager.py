from business_logic.model.Hogwarts import Hogwarts
from business_logic.model.Student import Student


class StudentManager:

    def __init__(self):
        self.hogwarts = Hogwarts()

    def add_student(self) -> None:
        first_name: str = input("First name: ")
        last_name: str = input("Last name: ")

        student: Student = Student(first_name, last_name)

        student.assign_house(self.hogwarts)

    def list_students(self) -> None:
        for house in self.hogwarts.houses:
            print(house.name)
            for student in house.students:
                print(f"{student.first_name} {student.last_name}")
