class Monster:
    def __init__(self, name, strength, mana, endurance, intelligence, agility, dexterity, luck, charisma, wisdom, health_points, drops={}, equipment={}):
        self.strength = strength
        self.mana = mana
        self.endurance = endurance
        self.intelligence = intelligence
        self.agility = agility
        self.dexterity = dexterity
        self.luck = luck
        self.charisma = charisma
        self.wisdom = wisdom
        self.hp = health_points
        self.equipment = equipment
        self.drops = drops # drops include materials, experience, items and equipment

   
    def calculate_hp(self):
        return self.endurance * 10