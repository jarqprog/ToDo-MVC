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
        # while True:
        #     self.view.display_menu_choices()
        #     self.view.display_custom_text("\n\n\n")
        #     self.set_choice(correct_choices, set_value=False)
        #     clear_screen()
        #     if self.choice == "1":
        #         self.view.display_simple_text(self.user.display_my_tasks())
        #     elif self.choice == "2":
        #         self.add_new_task()
        #     elif self.choice == "3":
        #         self.add_new_task()
        #     elif self.choice == "4":
        #         self.mark_task_as_done()
        #     elif self.choice == "5":
        #         self.mark_task_as_todo()
        #     elif self.choice == "0":
        #         self.exit_program()
        #     pause()

    # def remove_task(self, __user):
    #     text = __user + ", please type task's name (max 20 chars)."
    #     self.view.display_simple_text(text)
    #     name = input()
    #     text = __user + ", please type task's description (max 150 chars)."
    #     self.view.display_simple_text(text)
    #     description = input()
    #     self.user.tasks.add_task(name, description)
    #     lastly_added = -1  # last position (index) in list
    #     text = "Added new task:\n" + str(self.user.tasks.my_tasks[lastly_added])
    #     self.view.display_simple_text(text)

    def add_new_task(self, __user):
        text = __user + ", please type task's name (max 20 chars)."
        self.view.display_simple_text(text)
        name = input()
        text = __user + ", please type task's description (max 150 chars)."
        self.view.display_simple_text(text)
        description = input()
        self.user.tasks.add_task(name, description)
        lastly_added = -1  # last position (index) in list
        text = "Added new task:\n" + str(self.user.tasks.my_tasks[lastly_added])
        self.view.display_simple_text(text)

    def mark_task_as_done(self, __user):
        if self.user.tasks.my_tasks:
            task_id = self.take_task_id_from_user(__user)
            self.user.tasks.mark_task_as_done(task_id)
            self.display_info_about_completion_of_the_action(task_id)
        else:
            self.display_info_about_empty_tasks_list()

    def mark_task_as_todo(self, __user):
        if self.user.tasks.my_tasks:
            task_id = self.take_task_id_from_user(__user)
            self.user.tasks.mark_task_as_todo(task_id)
            self.display_info_about_completion_of_the_action(task_id)
        else:
            self.display_info_about_empty_tasks_list()

    def take_task_id_from_user(self, __user):
        self.view.display_simple_text(self.user.display_my_tasks())
        text = __user + ", please choose task (by id number):"
        self.view.display_simple_text(text)
        correct_choices = [str(x) for x in range(len(self.user.tasks.my_tasks))]
        self.set_choice(correct_choices, set_value=False)
        task_id = int(self.choice)
        return task_id

    def display_info_about_completion_of_the_action(self, task_id):
        text = "Done, updated task data:\n"
        self.view.display_simple_text(text + str(self.user.tasks.my_tasks[task_id]))

    def display_info_about_empty_tasks_list(self):
        text = "There's no task to display, You should create a task first."
        self.view.display_simple_text(text)

    def exit_program(self):
        self.view.say_goodbye(str(self.user.name))
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
