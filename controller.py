"""Controller in MVC structure."""

from user import User
from view import View, Menu, MenuOption, Other
from mytools import pause
from mytools import clear_screen
import data
import pickle


class Controller():
    """Takes data from Model and View, affects both."""

    menu_views = {}  # will contains views for both menus: init and main
    option_views = {}  # will contain views for options in both menus
    other_views = {}
    # data for views creation:
    init_choices_data = data.init_choices
    main_choices_data = data.main_choices
    other_views_data = data.other_views_data
    my_menus_data = data.my_menus

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

    @classmethod
    def set_my_init_option_views(cls):
        for option in cls.init_choices_data:
            cls.option_views[option] = MenuOption(cls.init_choices_data[option])

    @classmethod
    def set_my_menu_views(cls):
        for menu in cls.my_menus_data:
            cls.menu_views[menu] = Menu(
                                        choices=cls.my_menus_data[menu][0],
                                        special_choices=cls.my_menus_data[menu][1],
                                        is_main=cls.my_menus_data[menu][2])

    @classmethod
    def set_my_others_views(cls):
        for other in cls.other_views_data:
            cls.other_views[other] = Other(cls.other_views_data[other])

    @classmethod
    def set_my_all_views(cls):
        cls.set_my_init_option_views()
        cls.set_my_menu_views()
        cls.set_my_others_views()

    @classmethod
    def get_proper_option_view(cls, need_view_for):
        for view in cls.option_views:
            if view == need_view_for:
                return cls.option_views[view]

    @classmethod
    def get_proper_menu_view(cls, need_view_for):
        for view in cls.menu_views:
            if view == need_view_for:
                return cls.menu_views[view]

    @classmethod
    def get_proper_other_view(cls, need_view_for):
        for view in cls.other_views:
            if view == need_view_for:
                return cls.other_views[view]

    @classmethod
    def set_my_views_name(cls, name):
        for view in cls.menu_views:
            cls.menu_views[view].set_name(name)
        for view in cls.option_views:
            cls.option_views[view].set_name(name)
        for view in cls.other_views:
            cls.other_views[view].set_name(name)

    def __init__(self):
        self.set_my_all_views()
        intro = self.get_proper_other_view("intro")
        print(type(intro))
        init_menu = self.get_proper_menu_view("init")
        correct_choices = [str(num) for num in range(len(self.init_choices_data))]
        intro.display_intro()
        while True:
            init_menu.display()
            self.set_choice(correct_choices)
            clear_screen()
            if self.choice == "1":
                view = self.get_proper_option_view("Start with new profile")
                view.display_choosen_text_from_my_texts(animating=True)
                name = input()
                self.user = User(name)
                break
            elif self.choice == "2":
                self.user = self.load_user_profile()
                view = self.get_proper_option_view("Load profile")
                view.display_custom_text(text=self.user.name + ", User profile loaded.", animating=True)
                break
            else:
                view = self.get_proper_option_view("About program")
                view.display_choosen_text_from_my_texts(animating=True)
                pause()

        self.set_my_views_name(self.user.name)

    def menu_loop(self):
        """Execute main menu."""
        main_menu = self.get_proper_menu_view("main")
        main_menu.display_name_and_text(text=", what do you want to do?")
        correct_choices = [str(num) for num in range(len(self.main_choices_data))]
        correct_choices.append("I")  # for "get task id by task name" option
        correct_choices.append("S")  # for "save my profile" option
        while True:
            main_menu.display()
            self.set_choice(correct_choices)
            if self.choice == "1":
                display_tasks = self.get_proper_menu_view("display tasks")
                display_tasks.display_custom_text(self.user.get_all_my_tasks())
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
                outro = self.get_proper_other_view("outro")
                outro.display_outro()
                exit()
            pause()

    def add_new_task(self, add_new_task):
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
