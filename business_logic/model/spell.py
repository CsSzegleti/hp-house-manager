class Spell:
    def __init__(self, obj_id: int, name: str, complexity: int, damage: int, min_level: int, description: str):
        self.obj_id: int = obj_id
        self.name: str = name
        self.complexity: int = complexity
        self.damage: int = damage
        self.min_level: int = min_level
        self.description: str = description