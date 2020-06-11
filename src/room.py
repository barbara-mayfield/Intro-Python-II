# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def print_desc(self):
        return f"Description: {self.description}"

    def add_room_item(self, item):
        self.items.append(item)

    def __str__(self):
        return f"{self.name}: {self.description}"

    def __repr__(self):
        return f"{self.items}"
