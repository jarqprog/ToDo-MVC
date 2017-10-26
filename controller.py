"""Controller in MVC structure."""

from user import User
from view import View
from mytools import pause
from mytools import clear_screen


class Controller():

    menu_choices = ["display tasks",
                    "add task",
                    "remove task",
                    "mark task as done",
                    "mark task as todo",
                    "display task description",
                    "change task name",
                    "change task description",
                    "remove all tasks",
                    "exit program"]

    def __init__(self):
        self.view = View()
        self.view.display_intro()
        self.view.text = "Welcome in ToDo program. Please, enter Your name:"
        self.view.display_text()
        name = input()
        self.user = User(name)
        self.view.name = self.user.name
        self.view.menu_choices = self.menu_choices

    def menu_loop(self):
        self.view.text = ", what do you want to do?"
        self.view.display_name_and_text()
        correct_choices = [str(num) for num in range(len(self.menu_choices))]
        while True:
            self.view.display_menu_choices()
            self.view.display_custom_text("\n\n\n")
            self.set_choice(correct_choices, set_value=False)
            clear_screen()
            if self.choice == "1":
                self.view.display_custom_text(self.user.get_all_my_tasks())
            elif self.choice == "2":
                self.add_new_task()
            elif self.choice == "3":
                self.remove_task()
            elif self.choice == "4":
                self.mark_task_as_done()
            elif self.choice == "5":
                self.mark_task_as_todo()
            elif self.choice == "6":
                self.get_task_full_description()
            elif self.choice == "7":
                self.change_task_name()
            elif self.choice == "8":
                self.change_task_description()
            elif self.choice == "9":
                self.remove_all_tasks()
            elif self.choice == "0":
                self.exit_program()
            pause()

    def add_new_task(self):
        self.view.text = ", please type task's name (max 20 chars)."
        self.view.display_name_and_text()
        _name = input()
        self.view.text = ", please type task's description (max 150 chars)."
        self.view.display_name_and_text()
        _description = input()
        self.user.add_task(_name, _description)
        self.get_info_about_completion_of_the_action()

    def remove_task(self):
        if self.user.tasks.my_tasks:
            task_id = self.take_task_id_from_user()
            self.user.remove_task(task_id)
            self.get_info_about_completion_of_the_action()
        else:
            self.get_info_about_empty_tasks_list()

    def mark_task_as_done(self):
        if self.user.tasks.my_tasks:
            task_id = self.take_task_id_from_user()
            self.user.mark_task_as_done(task_id)
            self.get_info_about_completion_of_the_action()
        else:
            self.get_info_about_empty_tasks_list()

    def mark_task_as_todo(self):
        if self.user.tasks.my_tasks:
            task_id = self.take_task_id_from_user()
            self.user.mark_task_as_todo(task_id)
            self.get_info_about_completion_of_the_action()
        else:
            self.get_info_about_empty_tasks_list()

    def get_task_full_description(self):
        if self.user.tasks.my_tasks:
            task_id = self.take_task_id_from_user()
            self.view.text = self.user.get_task_full_description(task_id)
            self.view.display_text()
        else:
            self.get_info_about_empty_tasks_list()

    def change_task_name(self):
        if self.user.tasks.my_tasks:
            task_id = self.take_task_id_from_user()
            self.view.text = ", please type new task's name (max 20 chars)."
            self.view.display_name_and_text()
            _name = input()
            self.user.change_task_name(task_id, _name)
            self.get_info_about_completion_of_the_action()
        else:
            self.get_info_about_empty_tasks_list()

    def change_task_description(self):
        if self.user.tasks.my_tasks:
            task_id = self.take_task_id_from_user()
            self.view.text = ", please type task's description (max 150 chars)."
            self.view.display_name_and_text()
            _description = input()
            self.user.change_task_description(task_id, _description)
            self.get_info_about_completion_of_the_action()
        else:
            self.get_info_about_empty_tasks_list()

    def remove_all_tasks(self):
        self.user.remove_all_tasks()
        self.view.text = "tasks list is empty now"
        self.view.display_text()


    def take_task_id_from_user(self):
        self.view.display_custom_text(self.user.get_all_my_tasks())
        self.view.text = ", please choose task (by id number):"
        self.view.display_name_and_text()
        correct_choices = [str(x) for x in range(len(self.user.tasks.my_tasks))]
        self.set_choice(correct_choices, set_value=False)
        task_id = int(self.choice)
        return task_id

    def get_info_about_completion_of_the_action(self):
        self.view.text = "Done, updated tasks data:\n\n" + str(self.user.get_all_my_tasks())
        self.view.display_text()

    def get_info_about_empty_tasks_list(self):
        self.view.text = "There's no task to display, You should create a task first."
        self.view.display_text()

    def exit_program(self):
        self.view.say_goodbye()
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
                self.choice = input()
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
