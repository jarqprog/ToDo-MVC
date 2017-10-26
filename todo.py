"""Contain ToDo items class. In MVC it's part of Model."""


class ToDo():
    """Items ToDo class."""

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
        """
        self.name = self.set_proper_length_of_the_string(name, proper_length=20)
        self.description = self.set_proper_length_of_the_string(description, proper_length=150)
        self.is_done = False

    def __str__(self):
        return "name: " + self.name + ", is done: " + str(self.is_done) + ", description: " + self.description

    def set_new_name(self, new_name):
        self.name = self.set_proper_length_of_the_string(new_name, proper_length=20)

    def set_new_description(self, new_description):
        self.description = self.set_proper_length_of_the_string(new_description, proper_length=150)

    def mark_me_as_done(self):
        self.is_done = True

    def mark_me_as_todo(self):
        self.is_done = False
