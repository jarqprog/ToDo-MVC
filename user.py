"""Contains User class. In MVC structure it's part of Model."""

from todolist import ToDoList


class User():

    def __init__(self, name):
        self.name = name[:20].capitalize()
        self.tasks = ToDoList()

    def __str__(self):
        return str(self.name)

    def display_my_tasks(self):
        if self.tasks.my_tasks:
            return str(self.tasks)
        else:
            return "Don't have any task yet.."