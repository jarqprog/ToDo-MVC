"""Contain ToDo items class."""


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
            index_modifier = 1  # for correct indexing in cutting string process
            cut_index = proper_length + index_modifier
            modified_string = string[:cut_index]
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
