"""Controller in MVC structure."""

from user import User
from view import Menu, MenuOption, Other
from mytools import pause
from mytools import clear_screen
import data
import pickle


class Controller():
    """Takes data from Model and View, affects both."""

    menu_views = {}  # will contains Views for both menus: init and main
    option_views = {}  # will contain Views for options in both menus
    other_views = {}
    # data for Views creation:
    init_choices_data = data.init_choices
    main_choices_data = data.main_choices
    other_views_data = data.other_views_data
    my_menus_data = data.my_menus

    @staticmethod
    def take_input_from_user_clear_screen():
        while True:
            _input = input()
            if _input:
                clear_screen()
                return _input

    @classmethod
    def set_choice(cls, _correct_choices):
        """
        Support User inputs.

        When correct_choices is specified (list with available choices),
        check if User input is in list, set user choice from correct input (string type).
        """
        while True:
            cls.choice = input().upper()
            if _correct_choices:
                if cls.choice in _correct_choices:
                    break
            else:
                cls.other_views["set choice"].display_text_from_my_texts()

    @classmethod
    def load_user_profile(cls):
        with open('my_profile.save', 'rb') as input:
            user = pickle.load(input)
            return user

    @classmethod
    def set_init_option_views(cls):
        """Create Views used in initial menu, collect them in dictionary."""
        for option in cls.init_choices_data:
            cls.option_views[option] = MenuOption(option, cls.init_choices_data[option])

    @classmethod
    def set_main_option_views(cls):
        """Create Views used in main menu, collect them in dictionary."""
        for option in cls.main_choices_data:
            cls.option_views[option] = MenuOption(option, cls.main_choices_data[option])

    @classmethod
    def set_menu_views(cls):
        """Create Views for initial and main menu, collect them in dictionary."""
        for menu in cls.my_menus_data:
            cls.menu_views[menu] = Menu(
                                        menu,
                                        choices=cls.my_menus_data[menu][0],
                                        special_choices=cls.my_menus_data[menu][1],
                                        is_main=cls.my_menus_data[menu][2])

    @classmethod
    def set_others_views(cls):
        """Create additional Views for inner methods, collect them in dictionary."""
        for other in cls.other_views_data:
            cls.other_views[other] = Other(other, cls.other_views_data[other])

    @classmethod
    def set_all_views(cls):
        """Create all Views, collect them in dicts."""
        cls.set_init_option_views()
        cls.set_main_option_views()
        cls.set_menu_views()
        cls.set_others_views()

    @classmethod
    def set_my_views_name(cls, name):
        """Set name for all Views."""
        for view in cls.menu_views:
            cls.menu_views[view].set_name(name)
        for view in cls.option_views:
            cls.option_views[view].set_name(name)
        for view in cls.other_views:
            cls.other_views[view].set_name(name)

    def __init__(self):
        self.set_all_views()  # creates all needed Views
        _correct_choices = [str(num) for num in range(len(self.init_choices_data))]
        self.other_views["intro"].display_intro()
        while True:
            self.menu_views["init"].display()
            self.set_choice(_correct_choices)
            clear_screen()
            if self.choice == "1":
                self.option_views["Start with new profile"].display_text_from_my_texts()
                _name = self.take_input_from_user_clear_screen()
                self.user = User(_name)
                break
            elif self.choice == "2":
                self.user = self.load_user_profile()  # import User data from file
                self.option_views["Load profile"].display_text_from_my_texts(name=True)
                break
            else:
                self.option_views["About program"].display_text_from_my_texts()
                pause()

        self.set_my_views_name(self.user.name)  # all views can use user name now

    def menu_loop(self):
        """Execute main menu."""
        # get views for varied option:
        _correct_choices = [str(num) for num in range(len(self.main_choices_data))]
        _correct_choices.append("I")  # for "get task id by task name" option
        _correct_choices.append("S")  # for "save my profile" option
        while True:
            self.menu_views["main"].display()
            self.set_choice(_correct_choices)
            clear_screen()
            if self.choice == "1":
                _text = str(self.user.get_all_my_tasks())
                self.option_views["display tasks"].display_custom_text(_text)
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
                self.option_views["exit program"].display_text_from_my_texts(name=True, animating=True)
                exit()
            pause()

    def add_new_task(self):
        self.option_views["add task"].display_text_from_my_texts(name=True)
        while True:
            _name = self.take_input_from_user_clear_screen()
            if _name:
                break
        self.option_views["add task"].display_text_from_my_texts(chosen_index=1)
        _description = self.take_input_from_user_clear_screen()
        self.user.add_task(_name, _description)
        self.get_info_about_completion_of_the_action()

    def remove_task(self):  # Views in inner methods
        if self.user.tasks.my_tasks:
            task_id = self.take_task_id_from_user()
            self.user.remove_task(task_id)
            self.get_info_about_completion_of_the_action()
        else:
            self.get_info_about_empty_tasks_list()

    def mark_task_as_done(self):  # Views in inner methods
        if self.user.tasks.my_tasks:
            task_id = self.take_task_id_from_user()
            self.user.mark_task_as_done(task_id)
            self.get_info_about_completion_of_the_action()
        else:
            self.get_info_about_empty_tasks_list()

    def mark_task_as_todo(self):  # Views in inner methods
        if self.user.tasks.my_tasks:
            task_id = self.take_task_id_from_user()
            self.user.mark_task_as_todo(task_id)
            self.get_info_about_completion_of_the_action()
        else:
            self.get_info_about_empty_tasks_list()

    def get_task_full_description(self):
        if self.user.tasks.my_tasks:
            _task_id = self.take_task_id_from_user()
            _text_to_display = self.user.get_task_full_description(_task_id)
            self.option_views["display task description"].display_custom_text(_text_to_display)
        else:
            self.get_info_about_empty_tasks_list()

    def change_task_name(self):
        if self.user.tasks.my_tasks:
            _task_id = self.take_task_id_from_user()
            _text = "Current task data:\n\n" + self.user.get_task_name(_task_id)
            self.option_views["change task name"].display_custom_text(_text)
            self.option_views["change task name"].display_text_from_my_texts(name=True)
            _name = self.take_input_from_user_clear_screen()
            self.user.change_task_name(_task_id, _name)
            self.get_info_about_completion_of_the_action()
        else:
            self.get_info_about_empty_tasks_list()

    def change_task_description(self):
        if self.user.tasks.my_tasks:
            _task_id = self.take_task_id_from_user()
            _text = "Current task data:\n\n" + self.user.get_task_full_description(_task_id)
            self.option_views["change task description"].display_custom_text(_text)
            self.option_views["change task description"].display_text_from_my_texts(name=True)
            _description = self.take_input_from_user_clear_screen()
            self.user.change_task_description(_task_id, _description)
            self.get_info_about_completion_of_the_action()
        else:
            self.get_info_about_empty_tasks_list()

    def remove_all_tasks(self):
        self.user.remove_all_tasks()
        self.option_views["remove all tasks"].display_text_from_my_texts()

    def get_task_id_by_task_name(self):
        if self.user.tasks.my_tasks:
            self.option_views["get task id by task name"].display_text_from_my_texts(name=True)
            _task_name = self.take_input_from_user_clear_screen()
            _task_id = self.user.get_task_id_by_name(_task_name)
            self.option_views["get task id by task name"].display_custom_text("Task id:\n\n" + _task_id)
        else:
            self.get_info_about_empty_tasks_list()

    def save_user_profile_to_file(self):
        with open('my_profile.save', 'wb') as output:
            pickle.dump(self.user, output, pickle.HIGHEST_PROTOCOL)
            self.option_views["save my profile"].display_text_from_my_texts(name=True)

    def take_task_id_from_user(self):
        self.other_views["take task id"].display_custom_text(self.user.get_all_my_tasks())
        self.other_views["take task id"].display_text_from_my_texts(name=True)
        _correct_choices = [str(x) for x in range(len(self.user.tasks.my_tasks))]
        self.set_choice(_correct_choices)
        _task_id = int(self.choice)
        clear_screen()
        return _task_id

    def get_info_about_completion_of_the_action(self):
        clear_screen()
        self.other_views["succes"].display_text_from_my_texts()
        _text = str(self.user.get_all_my_tasks())
        self.other_views["succes"].display_custom_text(text=_text)

    def get_info_about_empty_tasks_list(self):
        self.other_views["failure"].display_text_from_my_texts(name=True)

    # I'm calling Views using dicts to slim down code,
    # but we can either call View using methods:
    def get_proper_option_view(self, need_view_for):
        for view in self.option_views:
            if view == need_view_for:
                return self.option_views[view]

    def get_proper_menu_view(self, need_view_for):
        for view in self.menu_views:
            if view == need_view_for:
                return self.menu_views[view]

    def get_proper_other_view(self, need_view_for):
        for view in self.other_views:
            if view == need_view_for:
                return self.other_views[view]
