from business_logic.duel_service import DuelService
from business_logic.model.spell import Spell
from presentation.menu import Menu
import time

player_keys = ['q', 'w', 'e', 'r', 't']


class DuelManager:
    def __init__(self):
        self.duel_service = DuelService()
        self.chosen_spell: None | Spell = None

    def duel(self):
        self.__player_spell_selector()
        cpu_player_spell = self.duel_service.choose_cpu_player_spell(self.duel_service.list_spells())
        cpu_player_cast_time = self.duel_service.cpu_player_cast_time(cpu_player_spell)
        player_cast_time = self.__cast_player_spell()

        print(f"Your time: {player_cast_time} | Opponent time: {cpu_player_cast_time}")

        if player_cast_time <= cpu_player_cast_time:
            print("You were faster, congratulations")
        else:
            print("You have lost")
        input("Press ENTER to continue...")

    def __choose_spell(self, spell: Spell, spell_menu: Menu):
        self.chosen_spell = spell
        spell_menu.deactivate()

    def __player_spell_selector(self):
        spells = self.duel_service.list_spells()
        spell_menu = Menu("Choose a spell")

        for spell in spells:
            spell_menu.add_menu_item(spell.name, self.__choose_spell, spell, spell_menu)

        spell_menu.activate()

    def __create_player_spell(self) -> str:
        expected_spell_keys = [""] * self.chosen_spell.complexity
        spell_keys: [int] = self.duel_service.craft_spell(self.chosen_spell)
        for idx, key in enumerate(spell_keys):
            expected_spell_keys[idx] = player_keys[key]

        return "".join(expected_spell_keys)

    def __cast_player_spell(self):
        expected_keys: str = self.__create_player_spell()
        print(f"Cast spell with: \"{expected_keys.upper()}\"")
        correct = False
        t0 = time.time()
        t1 = time.time()

        while not correct:
            input_keys = input()
            t1 = time.time()
            correct = self.__validate_input(expected_keys, input_keys)

        return t1 - t0

    def __validate_input(self, expected: str, actual: str):
        return expected == actual
