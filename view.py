"""Module contains class associated with the display in terminal."""

import mytools


class View():
    """Display varied info in terminal."""

    name = ""
    text = ""
    texts = ["", ""]

    def set_text(self, text):
        self.text = text

    def set_name(self, name):
        self.name = name

    @staticmethod
    def display_custom_text(text, animating=False):
        _string = '\n\n' + text + '\n'
        if animating:
            mytools.animate_string(string=_string)
        else:
            print(_string)

    def display_text(self, animating=False):
        _string = '\n\n' + self.text + '\n'
        if animating:
            mytools.animate_string(string=_string)
        else:
            print(_string)

    def display_choosen_text_from_my_texts(self, chosen_index=0, animating=False):
        _string = '\n\n\n' + self.texts[chosen_index] + '\n\n\n'
        if animating:
            mytools.animate_string(string=_string)
        else:
            print(_string)

    def display_name_and_text(self, text="", animating=False):
        _string = '\n\n' + self.name + self.text + text + '\n'
        if animating:
            mytools.animate_string(string=_string)
        else:
            print(_string)

    def display_graphics(self):
        if self.texts:
            mytools.clear_screen()
            try:
                mytools.display_text_with_asci_graphics(self.texts[0], self.texts[1])
            except:
                print("Missed second text..")
                mytools.pause()


class Menu(View):

    def __init__(self, choices, special_choices={}, is_main=False):
        self.choices = choices
        self.special_choices = special_choices  # choices that have own symbols in menu
        self.is_main = is_main  # bool, if True: display main menu, else: display initial menu

    def display(self):
        mytools.clear_screen()
        if self.is_main:
            self.display_custom_text(self.name + ", what do you want to do?")
        else:
            self.display_custom_text("Welcome in ToDo program. What do you want to do?")
        for number, choice in enumerate(self.choices):
            if choice not in self.special_choices.values():
                print("({}){:.>50}".format(number+1, choice))

        for choice in self.special_choices:
            print("({}){:.>50}".format(choice, self.special_choices[choice]))


class MenuOption(View):

    def __init__(self, texts):
        self.texts = texts


class Other(View):

    def __init__(self, texts):
        self.texts = texts

    def display_intro(self):
        mytools.clear_screen()
        self.display_graphics()
        mytools.pause()

    def display_outro(self):
        mytools.clear_screen()
        self.display_name_and_text(text=self.texts[0], animating=True)
