class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"


class Weapon(Item):
    def __init__(self, name, description, attack_range, damage):
        super().__init__(name, description)
        self.attack_range = attack_range
        self.damage = 0


stick = Item("stick", "it's just a stick")

dagger = Weapon("dagger", "a short, sharp blade", "close", 4)

print(stick)
print(dagger)
