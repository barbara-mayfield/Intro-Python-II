class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

    def __repr__(self):
        return f"{self.name}: {self.description}"


class Weapon(Item):
    def __init__(self, name, description, attack_range, damage):
        super().__init__(name, description)
        self.attack_range = attack_range
        self.damage = 0


class Treasure(Item):
    def __init__(self, name, description):
        super.__init__(name, description)


class LightSource(Item):
    def __init__(self, name, description, hasLight=True):
        super.__init__(name, description)
        self.hasLight = True

    def drop_item(self, item):
        if self.inventory.item.hasLight == True:
            self.inventory.remove(item)
            print(f"Though it is not wise, you have dropped {item}.")
