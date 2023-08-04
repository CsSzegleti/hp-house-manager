from business_logic.model.House import House, Houses


class Hogwarts:
    def __init__(self):
        self.houses = [
            House(Houses.GRYFFINDOR),
            House(Houses.RAVENCLAW),
            House(Houses.SLYTHERIN),
            House(Houses.HUFFLEPUFF)
        ]
