from player import Player

class Warrior(Player):
    def __init__(self, name="Warrior"):
        super().__init__(
            name=name,
            strength=10,
            mana=3,
            endurance=8,
            intelligence=4,
            agility=7,
            dexterity=9,  # Higher dex than Knight
            luck=5,
            charisma=5,
            wisdom=4
        )

    def power_strike(self):
        print(f"You performs a Power Strike using strength {self.strength}!")
