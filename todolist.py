"""Contains ToDoList class. In MVC structure it's Model."""

from todo import ToDo
from mytools import display_table_from_given_lists


class ToDoList():
    """Items ToDo list class. Contains all tasks (ToDo objects) and methods to manage them."""

    def __init__(self):
        self.my_tasks = []  # contains tasks (ToDo objects)

    def add_task(self, name, description):
        task_to_add = ToDo(name, description)
        self.my_tasks.append(task_to_add)

    def remove_task(self, id):
        try:
            id = abs(int(id))
        except ValueError:
            raise ValueError("id should be a number")
        del self.my_tasks[int(id)]

    def __str__(self):
        """Return content of my_items in string form (to display)."""
        head = ["id", "name", "description"]
        body = [[task.name, task.description] for task in self.my_tasks]
        return display_table_from_given_lists(head, body, bar_mark='-')


my_list = ToDoList()
my_list.add_task("kawa", "kawa jest do zrobienia")
my_list.add_task("herbatka", "herbatka jest do zrobienia")
my_list.add_task("woda", "woda jest do nalania")
print(my_list)
my_list.remove_task("-1")
print(my_list)
