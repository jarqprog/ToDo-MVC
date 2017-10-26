"""Controller in MVC."""

from todolist import ToDoList
from view import View


class Controller():

    view = View()
    menu_choices = []

    @classmethod
    def set_my_name(cls):
        name = "Jarek"
        user = User(name)
        return user

    def __init__(self):
        self.mytodo = ToDoList()
        self.myview = View()
        user = self.create_my_user()


class User(Controller):

    def __init__(self, name):
        self.name = name
