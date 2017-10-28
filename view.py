"""View in MVC architecture."""

import mytools


class View():
    """Parent class. Views are used to display info in terminal."""

    name = ""
    text = ""
    texts = ["", ""]
    uid = "Parent"

    def __str__(self):
        return self.uid

    def set_text(self, text):
        self.text = text

    def set_name(self, name):
        self.name = name

    @staticmethod
    def display_custom_text(text, animating=False):
        _string = '\n' + text + '\n\n'
        if animating:
            mytools.animate_string(string=_string)
        else:
            print(_string)

    def display_text_from_my_texts(self, name=False, chosen_index=0, animating=False):
        if name:
            _string = '\n' + self.name + ', ' + self.texts[chosen_index] + '\n\n'
        else:
            _string = '\n' + self.texts[chosen_index] + '\n\n'
        if animating:
            mytools.animate_string(string=_string)
        else:
            print(_string)

    def display_text(self, name=False, text="", animating=False):
        if name:
            _string = '\n' + self.name + self.text + text + '\n\n'
        else:
            _string = '\n' + self.text + text + '\n\n'
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
    """Views used to display menus."""

    def __init__(self, uid, choices, special_choices={}, is_main=False):
        self.uid = uid
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
        print("\n")


class MenuOption(View):
    """Views used to display menu options."""

    def __init__(self, uid, texts):
        self.uid = uid
        self.texts = texts


class Other(View):
    """Views used to display info in varied situations."""

    def __init__(self, uid, texts):
        self.uid = uid
        self.texts = texts

    def display_intro(self):
        mytools.clear_screen()
        self.display_graphics()
        mytools.pause()
