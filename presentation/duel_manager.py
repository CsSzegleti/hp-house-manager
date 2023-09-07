from business_logic.duel_service import DuelService
from business_logic.model.spell import Spell
from presentation.menu import Menu


class DuelManager:
    def __init__(self):
        self.duel_service = DuelService()
        self.chosen_spell: None | Spell = None

    def duel(self):
        spells = self.duel_service.list_spells()
        spell_menu = Menu("Choose a spell")

        for spell in spells:
            spell_menu.add_menu_item(spell.name, self.__choose_spell, spell, spell_menu)

        spell_menu.activate()

    def __choose_spell(self, spell: Spell, spell_menu: Menu):
        self.chosen_spell = spell
        spell_menu.deactivate()

