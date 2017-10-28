"""Contains data for controller, used to creating views."""

# initial menu options
init_choices = {"Start with new profile":
                ["Please, enter Your name:"],
                "Load profile":
                [", User profile loaded."],
                "About program":
                [("\n"*10) + "ToDo MVC program by jq for a Codecool assignment.\
                            \n27-10-2017 Cracow"]
                }

#
main_choices = {"display tasks":
                [""],
                "add task":
                [
                    ", please type task's name (max 20 chars).",
                    ", please type task's description (max 150 chars)."],
                "remove task":
                ["tasks list is empty now"],
                "mark task as done":
                ,
                "mark task as todo",
                "display task description",
                "change task name",
                "change task description",
                "remove all tasks",
                "get task id by task name",
                "save my profile",
                "exit program"]

# {"display tasks":
# #                 ,           # main menu options self.user.get_all_my_tasks()
# #                 "add task",
# #                 "remove task",
# #                 "mark task as done",
# #                 "mark task as todo",
# #                 "display task description",
# #                 "change task name",
# #                 "change task description",
# #                 "remove all tasks",
# #                 "get task id by task name",
# #                 "save my profile",
# #                 "exit program"}

other_views_data = {
                "intro":
                ["\nLoading Program...\n\n", "\nJupi! Program loaded ^o^\n"],
                "outro":
                [", goodbye!\n\n\nExit program...\n\n"],
                "helper":
                ["I'm just helper view ;)"],
                "succes":
                ["Done, updated tasks data:\n\n"],
                "failure":
                ["There's no task to display, You should create a task first."]}

my_menus = {"init":
            [[choice for choice in init_choices.keys()],
                {"0": "About program"},
                False],
            "main":
            [main_choices,
                {
                    "i": "get task id by task name",
                    "s": "save my profile",
                    "0": "exit program"},
                True]
            }
