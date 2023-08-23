from enum import Enum


class Houses(Enum):
    GRYFFINDOR = 0
    SLYTHERIN = 1
    RAVENCLAW = 2
    HUFFLEPUFF = 3


class House:
    def __init__(self, obj_id, name: Houses, points: int = 0):
        self.id = obj_id
        self.name = name
        self.students = []
        self.points = points



