"""Contains ToDoList class. In MVC structure it's Model."""

from todo import ToDo


class ToDoList():
    """Items ToDo list class. Contains all tasks (ToDo objects) and methods to manage them."""

    def __init__(self):
        self.my_items = []  # contains items ToDo

    def add_item(self, name, description):
        item_to_add = ToDo(name, description)
        self.my_items.append(item_to_add)

    def __str__(self):
        """Return content of items."""
        to_display = "%s, %s" % ("lp:", "item todo:".rjust(10))
        for number, item in enumerate(self.my_items):
            to_display += str(number), item + "\n"
        return to_display


my_list = ToDoList()
my_list.add_item("kawa", "kawa jest do zrobienia")
my_list.add_item("herbatka", "herbatka jest do zrobienia")
my_list.add_item("woda", "woda jest do nalania")



