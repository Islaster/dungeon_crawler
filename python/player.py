class Player:
    def __init__(self, strength = 5, mana = 5, endurance = 5, intelligence = 5, agility = 5, dexterity = 5, luck = 5, charisma = 5, wisdom = 5, experience = 0, expNeeded = 10,):
        self.strength = strength
        self.mana = mana
        self.endurance = endurance
        self.intelligence = intelligence
        self.agility = agility
        self.dexterity = dexterity
        self.luck = luck
        self.charisma = charisma
        self.wisdom = wisdom
        self.experience = experience
        self.expNeeded = expNeeded
        self.stat_points = 0
        self.level = 1
        self.hp = self.calculate_hp()
        self.inventory = []
        self.equipment = {}

    def calculate_hp(self):
        return self.endurance * 10

    def take_damage(self, amount):
        self.hp -= amount
        print(f"{self.name} takes {amount} damage. HP is now {self.hp}.")

    def level_up(self):
        self.level += 1
        self.experience = 0
        if self.level < 5:
            self.stat_points += 5
            print("acquired 5 stat points")
        else:
            self.stat_points += 3
            print("acquired 3 stat points")
        self.expNeeded += int(self.expNeeded * 0.25)
        self.hp = self.calculate_hp()
        print("leveled up 1!")
    def show_level(self):
        print(f"leveled up to ${self.level}")

    def gain_experience(self, amount):
        self.experience += amount
        print("Gained {amount} XP.")
        if self.experience >= self.expNeeded:
            self.level_up()
    
    def calculate_hit_points(self):
        hit_points = 1
        increase = (self.strength * 0.5) + (self.endurance * 0.5) + (self.agility * 0.5) + (self.dexterity * 0.5) + (self.wisdom * 0.5) + (self.intelligence * 0.5)
        hit_points += (increase // 10)
        return hit_points