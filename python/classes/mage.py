from player import Player

class Mage(Player):
    def __init__(self):
        super().__init__(
            strength=3,
            mana=15,
            endurance=4,
            intelligence=10,
            agility=6,
            dexterity=5,
            luck=5,
            charisma=6,
            wisdom=9
        )
    
    def calculate_hit_points(self):
        hit_points = 1
        increase = (self.wisdom * 0.5) + (self.intelligence * 0.5)
        hit_points += (increase // 10)

    def cast_spell(self, spell_name, cost):
        if self.mana >= cost:
            self.mana -= cost
            print(f"You cast {spell_name}! Remaining mana: {self.mana}")
        else:
            print(f"You don't have enough mana to cast {spell_name}.")

