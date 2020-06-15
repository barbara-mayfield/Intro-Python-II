from room import Room
# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, base_hp, current_room):
        self.name = name
        self.base_hp = base_hp
        self.profession = "Unemployed"
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
            print("Could not drop item")

    def __str__(self):
        return f"Player: {self.name}, {self.profession} \n Location: {self.current_room}"


class Profession:
    def __init__(self, title):
        self.title = title

    def set_hp(self, title):
        if self.title.lower() == "warrior":
            self.base_hp = 120
        elif self.title.lower() == "rogue":
            self.base_hp = 80
        elif self.title.lower() == "druid":
            self.base_hp = 110
        else:
            self.base_hp = 100

    def __str__(self):
        return f"{self.title}"
