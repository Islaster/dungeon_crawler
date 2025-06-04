import random

class Monster:
    def __init__(self, type, name, strength, mana, endurance, intelligence, agility, dexterity, luck, wisdom,  
                 drops={},
                 equipment = {
                    "armor": None,
                    "weapon": None,
                    "accessory": None
                },
                special_ability=None):
        self.name = name
        self.type = type
        self.strength = strength
        self.mana = mana
        self.endurance = endurance
        self.intelligence = intelligence
        self.agility = agility
        self.dexterity = dexterity
        self.luck = luck
        self.wisdom = wisdom
        self.hp = self.calculate_hp()
        self.equipment = equipment
        self.drops = drops # drops include materials, experience, items and equipment
        self.special_ability = special_ability

   
    def calculate_hp(self):
        return self.endurance * 10
    
    def calculate_def(self):
       base = (self.endurance* 0.25)
       equip = 0
       if self.equipment["armor"]:
           equip = self.equipment.armor.value // 10
       return base+equip
    
    def drop_rate(drops: list, percentage: float) -> list:
        return [item for item in drops if random.random() < percentage]
    
    def calculate_hit_points(self):
        hit_points = 0
        if self.type == "strength":
            hit_points = (self.strength*0.5) + (self.endurance * 0.5)
        elif self.type == "speed":
            hit_points = (self.agility *0.5) + (self.dexterity*0.5)
        elif self.type == "magic":
            hit_points = (self.wisdom*0.5) + (self.intelligence* 0.5)

        return 1 + (hit_points * 0.75)
