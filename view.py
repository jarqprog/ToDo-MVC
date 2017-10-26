"""Module contains class associated with the display in terminal."""

import mytools


class View():
    """Display varied info in terminal."""

    def __init__(self):
        self.name = ""
        self.text = ""
        self.intro_text_1 = "\nLoading Program...\n\n"
        self.intro_text_2 = "\nJupi! Program loaded ^o^\n"
        self.menu_choices = []
        self.excluded = "exit program"

    def display_intro(self):
        """Display simple intro."""
        mytools.clear_screen()
        mytools.display_text_with_asci_graphics(self.intro_text_1, self.intro_text_2)
        mytools.pause()

    def display_text(self):
        print('\n\n' + self.text, '\n')

    def display_name_and_text(self):
        print('\n\n' + self.name + self.text, '\n')

    def display_menu_choices(self):
        """
        Display enumerated elements from menu_choices list.

        Sample result:
        What do you want to do?
        (1) Choice1
        (2) Choice2
        (3) ...
        """
        mytools.clear_screen()
        self.display_custom_text(self.name + ", what do you want to do?")
        for number, choice in enumerate(self.menu_choices):
            if choice != self.excluded:
                print("({}){:.>50}".format(number+1, choice))
        print("({}){:.>50}".format(0, self.excluded))

    def say_goodbye(self):
        mytools.clear_screen()
        print("\n"*10)
        __string = ("\nGoodbye, " + self.name + "!\n\n\nExit program...\n\n")
        mytools.animate_string(string=__string)

    @staticmethod
    def display_custom_text(text):
        print('\n\n' + text, '\n')
