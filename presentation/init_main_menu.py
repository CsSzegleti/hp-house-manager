from presentation.duel_manager import DuelManager
from presentation.house_manager import HouseManager
from presentation.student_manager import StudentManager
from presentation.menu import Menu


def init_main_menu(student_manager: StudentManager, house_manager: HouseManager, duel_manager: DuelManager):
    # configure first sub menu - Student Manager
    sub_menu_student_manager = Menu("Student Manager", drawer_factory= Menu.Drawer)
    sub_menu_student_manager.add_menu_item("Add student", student_manager.add_student)
    sub_menu_student_manager.add_menu_item("List students", student_manager.list_students)
    sub_menu_student_manager.add_menu_item("Exit to main menu", sub_menu_student_manager.deactivate)

    # configure House manager submenu
    sub_menu_house_manager = Menu("House Manager", drawer_factory= Menu.Drawer)
    sub_menu_house_manager.add_menu_item("List houses", house_manager.list_houses)
    sub_menu_house_manager.add_menu_item("Exit to main menu", sub_menu_house_manager.deactivate)

    # configure the main menu
    main_menu = Menu("Main Menu", drawer_factory= Menu.Drawer)
    main_menu.add_menu_item("Student manager", sub_menu_student_manager.activate)
    main_menu.add_menu_item("House manager", sub_menu_house_manager.activate)
    main_menu.add_menu_item("Duel", duel_manager.duel)
    main_menu.add_menu_item("Exit program", main_menu.deactivate)

    # launch main menu
    main_menu.activate()
