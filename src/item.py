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
