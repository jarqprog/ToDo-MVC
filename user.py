"""Contains User class. In MVC structure it's part of Model."""

from todolist import ToDoList


class User():

    def __init__(self, name):
        self.name = name[:20].capitalize()
        self.tasks = ToDoList()

    def __str__(self):
        return self.name

    # def add_new_task(self):
    #     text = self.user_name + ", please type task's name (max 20 chars)."
    #     self.view.display_simple_text(text)
    #     name = input()
    #     text = self.user_name + ", please type task's description (max 150 chars)."
    #     self.view.display_simple_text(text)
    #     description = input()
    #     self.mytodo.add_task(name, description)
    #     lastly_added = -1  # last position (index) in list
    #     text = "Added new task:\n" + str(self.mytodo.my_tasks[lastly_added])
    #     self.view.display_simple_text(text)

    # def mark_task_as_done(self):
    #     if self.mytodo.my_tasks:
    #         self.view.display_tasks_in_table_format(self.mytodo)
    #         text = self.user_name + ", please choose task (by id) to mark as done:"
    #         self.view.display_simple_text(text)
    #         correct_choices = [str(x) for x in range(len(self.mytodo.my_tasks))]
    #         self.set_choice(correct_choices, set_value=False)
    #         index = int(self.choice)
    #         self.mytodo.mark_task_as_done(index)
    #         text = "Done, updated task data:\n"
    #         self.view.display_simple_text(text + str(self.mytodo.my_tasks[index]))
    #     else:
    #         text = "There's no task to display, You should create a task first."
    #         self.view.display_simple_text(text)

    # def display_tasks(self):
    #     if self.mytodo.my_tasks:
    #         self.view.display_tasks_in_table_format(self.mytodo)
    #     else:
    #         text = "There's no task to display, You should create a task first."
    #         self.view.display_simple_text(text)

user = User("jarek")

print(user)