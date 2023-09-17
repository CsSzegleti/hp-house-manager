import presentation.menu.console_utils as console
from presentation.menu.drawer import Drawer
from presentation.menu.drawer import MenuItem

UP_ARROW_KEY = '\x1b[A'
DOWN_ARROW_KEY = '\x1b[B'
ENTER_KEY = '\r'

DEFAULT_DECORATOR = '*'


class FunctionWithArgs:
    def __init__(self, func: callable, args):
        self.func = func
        self.args = args
        self.is_highlighted = False


class Menu:
    def __init__(self, name: str, drawer: Drawer):
        self.isActive = False
        self.items = dict()
        self.name = name
        self.drawer = drawer

    def add_menu_item(self, title: str, func: callable, *args):
        if title in self.items.keys():
            raise Exception("error.item.already.exist")

        self.items[title] = FunctionWithArgs(func, args)

    def draw_menu(self):
        console.clear_console()
        self.drawer.draw_header(self.name)
        self.drawer.draw_items([MenuItem(tag, value.is_highlighted) for (tag, value) in self.items.items()])

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

    def __read_user_input(self):
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
        _, selected_key = self.__get_selected()
        self.items[selected_key].func(*self.items[selected_key].args)

    def deactivate(self):
        selected_idx, selected_key = self.__get_selected()
        self.__dehighlight_menu_item(selected_idx)
        self.isActive = False

    def activate(self):
        self.isActive = True
        if len(self.items.keys()) > 0:
            self.__highlight_menu_item(0)
        while self.isActive:
            self.draw_menu()
            self.__read_user_input()
