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
        in_head_1 = "lp:"
        lenght_in_head_1 = len(in_head_1)
        in_head_2 = "item todo:"
        lenght_in_head_2 = len(in_head_2) + 40
    
        to_display = "{} {} \n".format(in_head_1, in_head_2)
        for number, item in enumerate(self.my_items):
            to_display += "{:02d} {} \n".format(number, str(item))
        return to_display


my_list = ToDoList()
my_list.add_item("kawa", "kawa jest do zrobienia")
my_list.add_item("herbatka", "herbatka jest do zrobienia")
my_list.add_item("woda", "woda jest do nalania")

print(my_list)
# print("%s, %s" % ("lp:", "item todo:".rjust(10)))
