# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move(self, direction, current_room):
        attribute = direction + "_to"

        if hasattr(current_room, attribute):
            return getattr(current_room, attribute)

        print("You cannot move in that direction.")

    def __str__(self):
        return f"Player: {self.name} \n Location: {self.current_room}"
