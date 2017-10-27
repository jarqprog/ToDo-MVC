"""Contains ToDoList class. In MVC structure it's component of Model."""

from todo import ToDo
from mytools import display_table_from_given_lists


class ToDoList():
    """Items ToDo list class. Contains all tasks (ToDo objects) and methods to manage them."""

    def __init__(self):
        self.my_tasks = []  # contains tasks (ToDo objects)
        first_task = ToDo("Explore this program", "Add and magane new tasks & have fun! Greetings from jq!")
        self.my_tasks.append(first_task)

    def __str__(self):
        """Return content of my_tasks in string form (to display)."""
        description_length = 50
        head = ["id", "task name", "is done?", "short description"]
        body = [
                [task.name, str(task.is_done), str(task.description[:description_length]+"...")]
                for task in self.my_tasks]
        return display_table_from_given_lists(head, body, bar_mark='-')  # mytools function

    def add_task(self, name, description):
        task_to_add = ToDo(name, description)
        self.my_tasks.append(task_to_add)
