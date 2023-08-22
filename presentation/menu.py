import os


class Menu:
    def __init__(self, name: str):
        self.isActive = False
        self.items = dict()
        self.name = name

    def add_menu_item(self, title: str, func: callable):
        if title in self.items.keys():
            raise Exception("error.item.already.exist")

        self.items[title] = func

    def draw_menu(self):
        os.system("clear")
        print()
        print(f"****{self.name}****")
        print()
        for idx, title in enumerate(self.items):
            print(f"{idx + 1} - {title}")

    def select(self):

        correct = False
        while not correct:
            user_input = input("Select menu item: ")
            try:
                int(user_input)
            except ValueError:
                continue
            selected_menu_item = int(user_input)
            if selected_menu_item <= len(self.items.keys()):
                correct = True

            if correct:
                for idx, title in enumerate(self.items):
                    if idx + 1 == selected_menu_item:
                        self.items[title]()
                        break

    def deactivate(self):
        self.isActive = False

    def activate(self):
        self.isActive = True
        while self.isActive:
            self.draw_menu()
            self.select()
