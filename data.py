"""Contains data for controller, used to creating views."""

init_options = {"Start with new profile":
                ["Please, enter Your name:"],
                "Load profile":
                [", User profile loaded."],
                "About program":
                [("\n"*10) + "ToDo MVC program by jq for a Codecool assignment.\
                            \n27-10-2017 Cracow"]
                }


main_options = {"display tasks":
                [""],
                "add task":
                [
                    "please type task's name (max 20 chars).",
                    "please type task's description (max 150 chars)."],
                "remove task":
                ["tasks list is empty now"],
                "mark task as done":
                [""],
                "mark task as todo":
                [""],
                "display task description":
                [""],
                "change task name":
                ["please type new task's name (max 20 chars)."],
                "change task description":
                ["please type task's description (max 150 chars)."],
                "remove all tasks":
                ["tasks list is empty now"],
                "get task id by task name":
                ["please type task's name. I'll show You id number."],
                "save my profile":
                ["User profile saved."],
                "exit program":
                ["goodbye!\n\nExit program...\n\n"]
                }

other_options = {
                "intro":
                ["\nLoading Program...\n\n", "\nJupi! Program loaded ^o^\n"],
                "take task id":
                ["please choose task (by id number):"],
                "succes":
                ["Done, updated tasks data:\r\r"],
                "failure":
                ["There's no task to display, You should create a task first."],
                "set choice":
                ["incorrect choice, try again.."]}

menu = {
                "init": [
                        init_options,
                        {"0": "About program"},
                        False],
                "main": [
                        main_options,
                        {"i": "get task id by task name",
                            "s": "save my profile",
                            "0": "exit program"},
                        True]
            }
