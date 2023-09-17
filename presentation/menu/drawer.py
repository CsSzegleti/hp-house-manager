class MenuItem:
     def __init__(self, tag: str, is_highlighted: bool):
          self.tag = tag
          self.is_highlighted = is_highlighted

class Drawer:

        def draw_header(self, header: str) -> None:
            print()
            print(header)
            print()
        
        def draw_items(self, items: [MenuItem]):
            for item in items:
                print(f"{self.highlight(item.tag) if item.is_highlighted else item.tag}")

        def highlight(self, string: str) -> str:
            return "\033[7m" + string + "\033[0m"
        
        def __len_to_full(self, tag: str) -> int:
            return self.__get_longest_tag_size() - len(tag)
        
        def __get_longest_tag_size(self):
            return max([len(tag) for tag in self.items.keys()])
        
