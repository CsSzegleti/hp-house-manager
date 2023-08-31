import os


class FunctionWithArgs:
    def __init__(self, func: callable, args):
        self.func = func
        self.args = args


class Menu:
    def __init__(self, name: str):
        self.isActive = False
        self.items = dict()
        self.name = name

    def add_menu_item(self, title: str, func: callable, *args):
        if title in self.items.keys():
            raise Exception("error.item.already.exist")

        self.items[title] = FunctionWithArgs(func, args)

    def draw_menu(self):
        os.system("clear")
        print(f"****{(len(self.name) + 2) * '*'}****")
        print(f"**** {self.name} ****")
        print(f"****{(len(self.name) + 2) * '*'}****")
        for idx, title in enumerate(self.items):
            print(f"{idx + 1} - {title}")

    def select(self):

        correct = False
        while not correct:
            user_input = input("Select menu item: ")
            correct = self.__validate_user_input(user_input)
            selected_menu_item = int(user_input)

            if correct:
                for idx, title in enumerate(self.items):
                    if idx + 1 == selected_menu_item:
                        self.items[title].func(*self.items[title].args)
                        break

    def deactivate(self):
        self.isActive = False

    def activate(self):
        self.isActive = True
        while self.isActive:
            self.draw_menu()
            self.select()

    def __validate_user_input(self, user_input: str) -> bool:
        try:
            int(user_input)
        except ValueError:
            return False

        if int(user_input) <= len(self.items.keys()):
            return True

        return False
