import random

import config
from business_logic.model.spell import Spell
from persistence.spell_repository import SpellRepository


class DuelService:
    def __init__(self):
        self.spell_repo = SpellRepository(config.database)  # TODO refactor this hidden dependency

    def list_spells(self):
        return self.spell_repo.list_spells()

    def craft_spell(self, spell: Spell) -> [int]:
        craft = []
        for i in range(spell.complexity):
            craft.append(random.randint(0, 3))

    def choose_cpu_player_spell(self, spells: [Spell]) -> Spell:
        if len(spells) > 0:
            return spells[random.randint(0, len(spells) - 1)]
        raise Exception("No available spells")

    def cpu_player_cast_time(self, spell: Spell):
        time = 0
        for i in range(spell.complexity):
            time += (random.random() + 0.5) % 1

        return time
