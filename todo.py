"""Contain ToDo items class."""


class ToDo():
    """Items ToDo class."""

    created_items_counter = 0  # number of created ToDo instancess

    @classmethod
    def check_if_string_has_proper_length(cls, string, proper_length=20):
        """Return bool."""
        string_length = len(string)
        if string_length <= proper_length:
            return True
        return False

    @classmethod
    def set_proper_length_of_the_string(cls, string, proper_length=20):
        """Cut string if it's too long. Returns string."""
        if cls.check_if_string_has_proper_length(string, proper_length) is False:
            modified_string = string[:proper_length]
            return modified_string
        return string

    def __init__(self, name, description):
        """
        Attributes:
        name: string, max 20 characters
        description: string, max 150 characters
        is_done: bool, False by default
        id: int
        """
        self.name = self.set_proper_length_of_the_string(name, proper_length=20)
        self.description = self.set_proper_length_of_the_string(description, proper_length=150)
        self.is_done = False
        self.id = ToDo.created_items_counter
        ToDo.created_items_counter += 1

    def __str__(self):
        return "id: " + str(self.id) + ", name: " + self.name + "description: " + self.description

    # def remove_me(self):
    #     __del__(self)

    def change_my_name(self, new_name):
        self.name = self.set_proper_length_of_the_string(new_name, proper_length=20)

    def change_my_description(self, new_description):
        self.description = self.set_proper_length_of_the_string(new_description, proper_length=150)

    def mark_me_as_done(self):
        self.is_done = True

# Modify item
# allow changing name
# allow changing description
# Delete item
# Mark item as done


task = ToDo("hjgfhajgsdasdashgdfashjgdfasdsahdgfgasdgfasdh12345", "opis")
# task1 = ToDo("kawa", "robienie kawy,     robienie kawy,     robienie kawy,     \
#                 robienie kawy,     robienie kawy,     robienie kawy,     robienie kawy,     \
#                 robienie kawy,     robienie kawy,     robienie kawy,     robienie kawy,     robienie kawy,     \
#                 robienie kawy,     robienie kawy,     robienie kawy,     robienie kawy,     robienie kawy,     \
#                 robienie kawy,     robienie kawy,     robienie kawy,     robienie kawy,     robienie kawy,     \
#                 mammmmmmma")
# print(task.name)
# print(len(task.name))
# print(task.description)
# print(task.id)
#
# print(task)
# print(task1)
# print(len(task1.description))
