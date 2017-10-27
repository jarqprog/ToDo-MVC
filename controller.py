"""Controller in MVC structure."""

from user import User
from view import View
from mytools import pause
from mytools import clear_screen
import pickle


class Controller():
    """Takes data from Model and View, affects both."""

    init_choices = ["Start with new profile",  # initial menu options
                    "Load profile",
                    "About program"]

    menu_choices = ["display tasks",           # main menu options
                    "add task",
                    "remove task",
                    "mark task as done",
                    "mark task as todo",
                    "display task description",
                    "change task name",
                    "change task description",
                    "remove all tasks",
                    "get task id by task name",
                    "save my profile",
                    "exit program"]

    view = View()

    @classmethod
    def set_choice(cls, correct_choices):
        """
        Support User inputs.

        When correct_choices is specified (list with available choices),
        check if User input is in list, set user choice from correct input (string type).
        """
        while True:
            cls.choice = input().upper()
            if correct_choices:
                if cls.choice in correct_choices:
                    break
            else:
                invalid_info = "incorrect choice, try again.."
                cls.view.display_custom_text(invalid_info)

    @classmethod
    def load_user_profile(cls):
        with open('my_profile.save', 'rb') as input:
            user = pickle.load(input)
            return user

    def __init__(self):
        self.view.display_intro()
        correct_choices = [str(num) for num in range(len(self.init_choices))]
        self.view.menu_choices = self.init_choices
        # initial menu (new profile, load profile, credits)
        while True:
            self.view.display_menu_choices()
            self.view.display_custom_text("\n\n\n")
            self.set_choice(correct_choices)
            clear_screen()
            if self.choice == "1":
                self.view.text = "Please, enter Your name:"
                self.view.display_text()
                name = input()
                self.user = User(name)
                self.view.name = self.user.name
                break
            elif self.choice == "2":
                self.user = self.load_user_profile()
                self.view.name = self.user.name
                self.view.text = ", User profile loaded."
                self.view.display_name_and_text()
                break
            else:
                self.view.display_credits()

        self.view.menu_choices = self.menu_choices

    def menu_loop(self):
        """Execute main menu."""
        self.view.text = ", what do you want to do?"
        self.view.display_name_and_text()
        correct_choices = [str(num) for num in range(len(self.menu_choices))]
        correct_choices.append("I")  # for "get task id by task name" option
        correct_choices.append("S")  # for "save my profile" option
        while True:
            self.view.display_menu_choices()
            self.view.display_custom_text("\n\n\n")
            self.set_choice(correct_choices)
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
            elif self.choice == "I":
                self.get_task_id_by_task_name()
            elif self.choice == "S":
                self.save_user_profile_to_file()
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

    def get_task_id_by_task_name(self):
        if self.user.tasks.my_tasks:
            self.view.text = ", please type task's name. I'll show You id number."
            self.view.display_name_and_text()
            _task_name = input()
            _task_id = self.user.get_task_id_by_name(_task_name)
            self.view.text = "Task id:\n\n" + _task_id
            self.view.display_text()
        else:
            self.get_info_about_empty_tasks_list()

    def save_user_profile_to_file(self):
        with open('my_profile.save', 'wb') as output:
            pickle.dump(self.user, output, pickle.HIGHEST_PROTOCOL)
            self.view.text = "User profile saved."
            self.view.display_text()

    def exit_program(self):
        self.view.say_goodbye()
        exit()

    def take_task_id_from_user(self):
        self.view.display_custom_text(self.user.get_all_my_tasks())
        self.view.text = ", please choose task (by id number):"
        self.view.display_name_and_text()
        correct_choices = [str(x) for x in range(len(self.user.tasks.my_tasks))]
        self.set_choice(correct_choices)
        task_id = int(self.choice)
        return task_id

    def get_info_about_completion_of_the_action(self):
        clear_screen()
        self.view.text = "Done, updated tasks data:\n\n" + str(self.user.get_all_my_tasks())
        self.view.display_text()

    def get_info_about_empty_tasks_list(self):
        self.view.text = "There's no task to display, You should create a task first."
        self.view.display_text()
