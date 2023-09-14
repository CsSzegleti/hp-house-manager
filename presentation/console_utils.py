import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def highlighted(string: str) -> str:
    return "\033[7m" + string + "\033[0m"


def __get_char_windows():
    import msvcrt
    return msvcrt.getch()


def __get_char_unix():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
        if ch == '\x1b':
            ch += sys.stdin.read(2)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def get_char():
    return __get_char_windows() if os.name == 'nt' else __get_char_unix()
