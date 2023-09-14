import sys

from presentation.duel_manager import DuelManager
from presentation.house_manager import HouseManager
from presentation.student_manager import StudentManager
from presentation.init_main_menu import init_main_menu as main_menu
from inint_db import init_db


if __name__ == '__main__':
    if "--init-db" in sys.argv:
        init_db()

    student_manager = StudentManager()
    house_manager = HouseManager()
    duel_manager = DuelManager()

    main_menu(student_manager,house_manager, duel_manager)
