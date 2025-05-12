import random

class Monster:
    def __init__(self, name, strength, mana, endurance, intelligence, agility, dexterity, luck, wisdom, health_points, 
                 drops={}, 
                 equipment={}, 
                 special_ability=None):
        self.name = name
        self.strength = strength
        self.mana = mana
        self.endurance = endurance
        self.intelligence = intelligence
        self.agility = agility
        self.dexterity = dexterity
        self.luck = luck
        self.wisdom = wisdom
        self.hp = health_points
        self.equipment = equipment
        self.drops = drops # drops include materials, experience, items and equipment
        self.special_ability = special_ability

   
    def calculate_hp(self):
        return self.endurance * 10
    
    def calculate_def(self):
       base = (self.endurance* 0.25)
       equip = 0
       if self.equipment.armor:
           equip = self.equipment.armor.value
       return base+equip
    
    def drop_rate(drops: list, percentage: float) -> list:
        return [item for item in drops if random.random() < percentage]
