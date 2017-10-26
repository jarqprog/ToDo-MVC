"""Module contains class associated with the display in terminal."""

import mytools


class View():
    """Display varied info in terminal."""

    @staticmethod
    def display_intro(text_1=None, text_2=None):
        """Display simple intro."""
        mytools.clear_screen()
        if text_1 is None:
            text_1 = "\nLoading Program...\n"
        if text_2 is None:
            text_2 = "Jupi! Program loaded ^o^\n"
        mytools.display_text_with_asci_graphics(text_1, text_2)
        mytools.pause()

    @staticmethod
    def display_simple_text(text):
        print('\n\n' + text, '\n')

    @staticmethod
    def display_menu_choices(head, menu_choices):
        """
        Display enumerated elements from menu_choices list.

        Sample result:
        What do you want to do?
        (1) Choice1
        (2) Choice2
        (3) ...
        """
        mytools.clear_screen()
        excluded = "exit program"
        print("\n\n" + head, "\n")
        for number, choice in enumerate(menu_choices):
            if choice != excluded:
                print("({}){:.>50}".format(number+1, choice))
        print("({}){:.>50}".format(0, excluded))

    @staticmethod
    def say_goodbye(name, string=None):
        mytools.clear_screen()
        print("\n"*10)
        if string is None:
            string = ("\nGoodbye, " + name + "!\n\n\nExit program...\n\n")
        mytools.animate_string(string=string)

    @staticmethod
    def display_tasks_in_table_format(tasks):
        mytools.clear_screen()
        print(tasks)
