"""Contains data for controller."""


        #
        # self.intro_text_1 = "\nLoading Program...\n\n"
        # self.intro_text_2 = "\nJupi! Program loaded ^o^\n"
        # self.menu_choices = []
        # self.excluded_1 = "get task id by task name"  # used to properly display menu
        # self.excluded_2 = "save my profile"  # used to properly display menu
        # self.excluded_3 = "exit program"  # used to properly display menu
        # self.excluded_4 = "About program"  # used to properly display initial menu




#                     choices=self.init_choices,
#                     special_choices={"0": "About program"},
#                     is_main=False)
#
intro_texts = ["\nLoading Program...\n\n", "\nJupi! Program loaded ^o^\n"]

# initial menu options
init_choices = {"Start with new profile":
                ["Please, enter Your name:"],
                "Load profile":
                [", User profile loaded."],
                "About program":
                [("\n"*10) + "ToDo MVC program by jq for a Codecool assignment.\
                            \n27-10-2017 Cracow"]
                }


menu_choices = {"display tasks",           # main menu options
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
                "exit program"}

my_menus = {"init":
            [[choice for choice in init_choices.keys()],
                {"0": "About program"},
                False],
            "menu":
            [menu_choices,
                {"0": "About program"},
                True]
            }



        # self.excluded_1 = "get task id by task name"  # used to properly display menu
        # self.excluded_2 = "save my profile"  # used to properly display menu
        # self.excluded_3 = "exit program"  # used to properly display menu
