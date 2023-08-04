from business_logic.model.Hogwarts import Hogwarts
from business_logic.model.Student import Student

if __name__ == '__main__':
    hogwarts: Hogwarts = Hogwarts()
    student: Student = Student("Susan", "Smith")

    print(student.house)

    student.assign_house(hogwarts)
    print(student.house.name)

    student.add_house_points(5)
    student.add_house_points(10)
    student.add_house_points(2)

    student.assign_house(hogwarts)
    print(student.house.name)
    student.add_house_points(10)
    student.add_house_points(10)
    student.assign_house(hogwarts)
    print(student.house.name)
    student.remove_house_points(5)

    print("House points")
    for house in hogwarts.houses:
        print(f"{house.name} - {house.points}")

