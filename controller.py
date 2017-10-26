"""Controller in MVC."""

from todolist import ToDoList
from view import View
from mytools import pause


class Controller():

    view = View()
    menu_choices = ["display tasks",
                    "display task description",
                    "add task",
                    "remove task",
                    "mark task as done",
                    "mark task as todo",
                    "change task name",
                    "change task description",
                    "exit program"]

    invitation = "Welcome in ToDo program. Please, enter Your name:"
    choice = ""

    @classmethod
    def set_user_name(cls):
        cls.view.display_simple_text(cls.invitation)
        return input()

    def __init__(self):
        self.mytodo = ToDoList()
        self.user_name = self.set_user_name()

    def menu_loop(self):
        head = self.user_name + ", what do you want to do?"
        correct_choices = [str(x) for x in range(len(self.menu_choices))]
        while True:
            self.view.display_menu_choices(head, self.menu_choices)
            self.set_choice(correct_choices, set_value=False)
            if self.choice == "1":
                self.display_tasks()
            elif self.choice == "3":
                self.add_new_task()
            elif self.choice == "0":
                self.exit_program()

    def add_new_task(self):
        text = self.user_name + ", please type task's name (max 20 chars)."
        self.view.display_simple_text(text)
        name = input()
        text = self.user_name + ", please type task's description (max 150 chars)."
        self.view.display_simple_text(text)
        description = input()
        self.mytodo.add_task(name, description)
        text = "Added new task: " + str(self.mytodo.my_tasks[-1])
        self.view.display_simple_text(text)
        pause()

    def mark_task_as_done(self):
        # view, input id
        # functions
        pass

    # def mark_task_as_done(self, id):
    #     self.my_tasks[id].mark_me_as_done()

    def display_tasks(self):
        if self.mytodo.my_tasks:
            self.view.display_tasks_in_table_format(self.mytodo)
        else:
            text = "There's no task to display, You should create a task first."
            self.view.display_simple_text(text)
            pause()

    def exit_program(self):
        self.view.say_goodbye(self.user_name)
        exit()

    def set_choice(self, correct_choices=None, set_value=False):
            """
            Support User inputs.

            Work in two modes:
            1) correct choices:
                when correct_choices is specified (list with available choices),
                check if User input is in list, return correct input (string type).
            2) set value mode:
                if set_value is True:
                    used to return float numbers
                    check if user input is float
                    returns input.
            """
            while True:
                text = self.user_name + ", please, type Your choice:"
                self.view.display_simple_text(text)
                self.choice = input("\n---> ")
                invalid_info = "incorrect choice, try again.."
                # 1. mode (check if input in correct_choices):
                if correct_choices:
                    if self.choice in correct_choices:
                        break
                # 2. mode (check if input in correct_choices):
                if set_value:
                    try:
                        self.choice = float(self.choice)
                        if self.choice > 0:
                            break
                        else:
                            self.view.display_simple_text("value should be positive number, try again..")
                    except:
                        self.view.display_simple_text(invalid_info)
                else:
                    self.view.display_simple_text(invalid_info)

    # def manage_main_menu(self):
    #     """Display menu (main options). User make's a choice."""
    #     self.display_menu_choices()  # display main menu
    #
    #     self.set_user_choice(correct_choices)
#
# class User(Controller):
#
#     def __init__(self, name):
#         self.name = name
