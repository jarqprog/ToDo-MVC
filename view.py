"""Module contains class associated with the display in terminal."""

import mytools


class View():
    """Display varied info in terminal."""

    @staticmethod
    def display_intro(text_1=None, text_2=None):
        """Display simple intro."""
        if text_1 is None:
            text_1 = "\nLoading Program...\n"
        if text_2 is None:
            text_2 = "\nGeometry loaded ^o^\n"
        mytools.display_text_with_asci_graphics(text_1, text_2)

    def display_menu_choices(self):
        """
        Display enumerated elements from menu_choices list.

        Sample result:
        What do you want to do?
        (1) Add new shape
        (2) Show all shapes
        (3) ...
        """
        excluded = "Exit program"
        print("\n\nWhat do you want to do?\n")
        for number, choice in enumerate(self.menu_choices):
            if choice != excluded:
                print("({}){:.>50}".format(number+1, choice))
        print("({}){:.>50}".format(0, excluded))


    def display_tasks_in_table_format(self, tasks):
        print(content)

    @staticmethod
    def welcome_user():
        print()
