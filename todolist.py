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

    def remove_task(self, uid):
        del self.my_tasks[uid]

    def change_task_name(self, uid, new_name):
        self.my_tasks[uid].set_new_name(new_name)

    def change_task_description(self, uid, new_description):
        self.my_tasks[uid].set_new_description(new_description)

    def mark_task_as_done(self, uid):
        self.my_tasks[uid].mark_me_as_done()

    def mark_task_as_todo(self, uid):
        self.my_tasks[uid].mark_task_as_todo()

    def display_task_name(self, uid):
        """Return string."""
        return self.my_tasks[uid].name

    def display_task_full_description(self, uid):
        """Return string."""
        return str(self.my_tasks[uid].name + ":\n" + self.my_tasks[uid].description)

    def get_task_id_by_name(self, name):
        """Return string."""
        for uid, task in enumerate(self.my_tasks):
            if task.name == name:
                return str(uid)
        return name + " - there's no such name in tasks list, type correct name..."

    def __str__(self):
        """Return content of my_items in string form (to display)."""
        description_length = 50
        head = ["id", "task name", "is done?", "short description"]
        body = [
                [task.name, str(task.is_done), str(task.description[:description_length]+"...")]
                for task in self.my_tasks]
        return display_table_from_given_lists(head, body, bar_mark='-')
#
#
# my_list = ToDoList()
# my_list.add_task("kawa", "kawa jest do zrobienia")
# my_list.add_task("herbatka", "herbatka jest do zrobienia")
# my_list.add_task("woda", "woda jest do nalania")
# print(my_list)
# my_list.remove_task(1)
# print(my_list)
# my_list.change_task_name(0, "coca cola")
# my_list.mark_task_as_done(0)
# my_list.change_task_description(1, "jest bardzo zdrowa i wyjątkowo smaczna, szczególnie ciepła, ponieważ rozgrzewa ciało i umysł jest bardzo zdrowa i wyjątkowo smaczna, szczególnie ciepła, ponieważ rozgrzewa ciało i umysł jest bardzo zdrowa i wyjątkowo smaczna, szczególnie ciepła, ponieważ rozgrzewa ciało i umysł jest bardzo zdrowa i wyjątkowo smaczna, szczególnie ciepła, ponieważ rozgrzewa ciało i umysł")
# print(my_list)
# print(my_list.display_task_name(1))
# print(my_list.display_task_full_description(1))
# print(my_list.get_task_id_by_name("pepsi cola"))
# print(my_list.my_tasks[0])
