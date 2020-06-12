# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.w_to = None
        self.e_to = None
        self.s_to = None

    def print_desc(self):
        return f"Description: {self.description}"

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        return f"{self.name}: {self.description}"

    def __repr__(self):
        return f"{self.items}"
