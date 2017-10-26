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

    def remove_task(self, task_id):
        del self.tasks.my_tasks[task_id]

    def change_task_name(self, task_id, new_name):
        self.tasks.my_tasks[task_id].set_new_name(new_name)

    def change_task_description(self, task_id, new_description):
        self.tasks.my_tasks[task_id].set_new_description(new_description)

    def mark_task_as_done(self, task_id):
        self.tasks.my_tasks[task_id].mark_me_as_done()

    def mark_task_as_todo(self, task_id):
        self.tasks.my_tasks[task_id].mark_me_as_todo()

    def get_task_name(self, task_id):
        """Return string."""
        return self.tasks.my_tasks[task_id].name

    def get_task_full_description(self, task_id):
        """Return string."""
        return str(self.tasks.my_tasks[task_id].name + ":\n" + self.tasks.my_tasks[task_id].description)

    def get_task_id_by_name(self, name):
        """Return string."""
        for task_id, task in enumerate(self.tasks.my_tasks):
            if task.name == name:
                return str(task_id)
        return name + " - there's no such name in tasks list, type correct name..."

    def get_all_my_tasks(self):
        """Return string."""
        if self.tasks.my_tasks:
            return str(self.tasks)
        else:
            return "Don't have any task yet.."

    def remove_all_tasks(self):
        del self.tasks.my_tasks[:]
