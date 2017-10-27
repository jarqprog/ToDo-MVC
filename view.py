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
        self.excluded_1 = "get task id by task name"  # used to properly display menu
        self.excluded_2 = "save my profile"  # used to properly display menu
        self.excluded_3 = "exit program"  # used to properly display menu
        self.excluded_4 = "About program"  # used to properly display initial menu

    def display_intro(self):
        mytools.clear_screen()
        mytools.display_text_with_asci_graphics(self.intro_text_1, self.intro_text_2)
        mytools.pause()

    @staticmethod
    def display_credits():
        mytools.clear_screen()
        print("\n"*10)
        __string = "ToDo MVC program by jq for a Codecool assignment.\
                    \n27-10-2017 Cracow"
        mytools.animate_string(string=__string)
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
        if self.name:
            self.display_custom_text(self.name + ", what do you want to do?")
        else:
            self.display_custom_text("Welcome in ToDo program. What do you want to do?")
        for number, choice in enumerate(self.menu_choices):
            if choice not in (self.excluded_1, self.excluded_2, self.excluded_3, self.excluded_4):
                print("({}){:.>50}".format(number+1, choice))
        if self.name:
            print("({}){:.>50}".format('i', self.excluded_1))
            print("({}){:.>50}".format('s', self.excluded_2))
            print("({}){:.>50}".format(0, self.excluded_3))
        else:
            print("({}){:.>50}".format(0, self.excluded_4))

    def say_goodbye(self):
        mytools.clear_screen()
        print("\n"*10)
        __string = ("\nGoodbye, " + self.name + "!\n\n\nExit program...\n\n")
        mytools.animate_string(string=__string)

    @staticmethod
    def display_custom_text(text):
        print('\n\n' + text, '\n')
