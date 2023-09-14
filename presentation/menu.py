import presentation.console_utils as console

UP_ARROW_KEY = '\x1b[A'
DOWN_ARROW_KEY = '\x1b[B'
ENTER_KEY = '\r'


class FunctionWithArgs:
    def __init__(self, func: callable, args):
        self.func = func
        self.args = args
        self.is_highlighted = False


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
        console.clear_console()
        print(f"****{(len(self.name) + 2) * '*'}****")
        print(f"**** {self.name} ****")
        print(f"****{(len(self.name) + 2) * '*'}****")
        for idx, title in enumerate(self.items):
            print(f"{console.highlighted(title) if self.items[title].is_highlighted else title}")

    def __get_selected(self):
        for idx, (key, value) in enumerate(self.items.items()):
            if value.is_highlighted:
                return idx, key

    def __move_select_up(self):
        selected_idx, selected_key = self.__get_selected()
        if selected_idx >= 1:
            self.__dehighlight_menu_item(selected_idx)
            self.__highlight_menu_item(selected_idx - 1)
            self.draw_menu()

    def __move_select_down(self):
        selected_idx, selected_key = self.__get_selected()
        if selected_idx <= len(self.items.keys()) - 2:
            self.__dehighlight_menu_item(selected_idx)
            self.__highlight_menu_item(selected_idx + 1)
            self.draw_menu()

    def read_user_input(self):
        user_input = console.get_char()
        if user_input == UP_ARROW_KEY:
            self.__move_select_up()
        if user_input == DOWN_ARROW_KEY:
            self.__move_select_down()
        if user_input == ENTER_KEY:
            self.select()

    def __highlight_menu_item(self, idx):
        list(self.items.values())[idx].is_highlighted = True

    def __dehighlight_menu_item(self, idx):
        list(self.items.values())[idx].is_highlighted = False

    def select(self):
        selected_idx, selected_key = self.__get_selected()
        self.items[selected_key].func(*self.items[selected_key].args)

    def deactivate(self):
        self.isActive = False

    def activate(self):
        self.isActive = True
        if len(self.items.keys()) > 0:
            self.__highlight_menu_item(0)
        while self.isActive:
            self.draw_menu()
            self.read_user_input()
            # self.select()

    def __validate_user_input(self, user_input: str) -> bool:
        try:
            int(user_input)
        except ValueError:
            return False

        if int(user_input) <= len(self.items.keys()):
            return True

        return False
