import presentation.console_utils as console

UP_ARROW_KEY = '\x1b[A'
DOWN_ARROW_KEY = '\x1b[B'
ENTER_KEY = '\r'

DEFAULT_DECORATOR = '*'


class FunctionWithArgs:
    def __init__(self, func: callable, args):
        self.func = func
        self.args = args
        self.is_highlighted = False


def sanitize_decorator(decorator: str) -> str:
    if len(decorator) > 1:
        return decorator[0]
    else:
        return decorator


class Menu:
    def __init__(self, name: str, decorator: str = '*', padding: int = 3):
        self.isActive = False
        self.items = dict()
        self.name = name
        self.decorator = sanitize_decorator(decorator)
        self.padding = padding

    def add_menu_item(self, title: str, func: callable, *args):
        if title in self.items.keys():
            raise Exception("error.item.already.exist")

        self.items[title] = FunctionWithArgs(func, args)

    def draw_menu(self):
        console.clear_console()
        if len(self.decorator) > 0:
            print(f"{self.padding * self.decorator}{(len(self.name) + 2) * self.decorator}{self.padding * self.decorator}")
        print(f"{self.padding * self.decorator}{len(self.decorator) * ' '}{self.name}{len(self.decorator) * ' '}{self.padding * self.decorator}")
        if len(self.decorator) > 0:
            print(f"{self.padding * self.decorator}{(len(self.name) + 2) * self.decorator}{self.padding * self.decorator}")
        print()
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
        selected_idx, selected_key = self.__get_selected()
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
