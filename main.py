from presentation.student_manager import StudentManager
from presentation.menu import Menu

if __name__ == '__main__':

    student_manager = StudentManager()

    # configure first sub menu - Student Manager
    sub_menu_student_manager = Menu("Student Manager")
    sub_menu_student_manager.add_menu_item("Add student", student_manager.add_student)
    sub_menu_student_manager.add_menu_item("List students", student_manager.list_students)
    sub_menu_student_manager.add_menu_item("Exit to main menu", sub_menu_student_manager.deactivate)

    # configure the main menu
    main_menu = Menu("Main Menu")
    main_menu.add_menu_item("Student manager", sub_menu_student_manager.activate)
    main_menu.add_menu_item("Exit program", main_menu.deactivate)

    # launch main menu
    main_menu.activate()

