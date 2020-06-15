from room import Room
# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
        self.game_over = False

    def move(self, direction, current_room):
        attribute = direction + "_to"

        if hasattr(current_room, attribute):
            return getattr(current_room, attribute)

        # Print an error message if the movement isn't allowed.
        else:
            print("You cannot move in that direction.")

        return current_room

    # add item to inventory
    def get_item(self, item):
        if self.current_room.items:
            self.remove_item(item)
            self.inventory.append(item)
            print(f"You have picked up {item}.")
        else:
            print(f"Cannot get item")

    # drop item from inventory
    def drop_item(self, item):
        self.inventory.remove(item)
        print(f"You have dropped {item}.")

    def remove_item(self, item):
        if self.current_room.items:
            for item in self.current_room.items:
                self.current_room.items.remove(item)
        else:
            print("Could not remove item")

    def __str__(self):
        return f"Player: {self.name} \n Location: {self.current_room}"
