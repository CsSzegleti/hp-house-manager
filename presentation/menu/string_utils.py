
def __pad_left(string: str, num_spaces: int) -> str:
    return num_spaces * ' ' + string


def __pad_right(string: str, num_spaces: int) -> str:
    return string + num_spaces * ' '
