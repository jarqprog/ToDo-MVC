"""Contains User class. In MVC structure it's component of Model."""

from todolist import ToDoList


class User():

    def __init__(self, name):
        self.name = name[:20].capitalize()
        self.tasks = ToDoList()

    def __str__(self):
        return str(self.name)

    def add_task(self, name, description):
        self.tasks.add_task(name, description)

    def remove_task(self, uid):
        del self.tasks.my_tasks[uid]

    def change_task_name(self, uid, new_name):
        self.tasks.my_tasks[uid].set_new_name(new_name)

    def change_task_description(self, uid, new_description):
        self.tasks.my_tasks[uid].set_new_description(new_description)

    def mark_task_as_done(self, uid):
        self.tasks.my_tasks[uid].mark_me_as_done()

    def mark_task_as_todo(self, uid):
        self.tasks.my_tasks[uid].mark_me_as_todo()

    def get_task_name(self, uid):
        """Return string."""
        return self.tasks.my_tasks[uid].name

    def get_task_full_description(self, uid):
        """Return string."""
        return str(self.tasks.my_tasks[uid].name + ":\n" + self.tasks.my_tasks[uid].description)

    def get_task_id_by_name(self, name):
        """Return string."""
        for uid, task in enumerate(self.tasks.my_tasks):
            if task.name == name:
                return str(uid)
        return name + " - there's no such name in tasks list, type correct name..."

    def get_all_my_tasks(self):
        """Return string."""
        if self.tasks.my_tasks:
            return str(self.tasks)
        else:
            return "Don't have any task yet.."
