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
    def __init__(self, name: str, drawer_factory: callable):
        self.isActive = False
        self.items = dict()
        self.name = name
        self.drawer = drawer_factory(self)

    class Drawer:
        def __init__(self, menu):
            self.menu = menu

        def draw_header(self):
            print()
            print(self.menu.name)
            print()
        
        def draw_items(self):
            for tag in self.menu.items:
                print(f"{console.highlighted(tag) if self.menu.items[tag].is_highlighted else tag}")

        def highlight(self, string: str) -> str:
            return "\033[7m" + string + "\033[0m"
        
        def __len_to_full(self, tag: str) -> int:
            return self.__get_longest_tag_size() - len(tag)
        
        def __get_longest_tag_size(self):
            return max([len(tag) for tag in self.items.keys()])
        
        def __pad_left(self, string: str, num_spaces: int) -> str:
            return num_spaces * ' ' + string

        def __pad_right(self, string: str, num_spaces: int) -> str:
            return string + num_spaces * ' '


    def add_menu_item(self, title: str, func: callable, *args):
        if title in self.items.keys():
            raise Exception("error.item.already.exist")

        self.items[title] = FunctionWithArgs(func, args)

    def draw_menu(self):
        console.clear_console()
        self.drawer.draw_header()
        self.drawer.draw_items()

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
