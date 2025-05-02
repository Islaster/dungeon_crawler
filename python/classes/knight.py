from player import Player

class Knight(Player):
    def __init__(self, name="Knight"):
        super().__init__(
            name=name,
            strength=13,     # Higher than Warrior
            mana=2,
            endurance=10,
            intelligence=3,
            agility=5,
            dexterity=6,     # Lower than Warrior
            luck=4,
            charisma=6,
            wisdom=5
        )

    def shield_block(self):
        print(f"You raises a shield to block incoming damage!")

    def calculate_hit_points(self):
        hit_points = 1
        increase = (self.strength * 0.5) + (self.endurance * 0.5)
        hit_points += (increase // 10)