from items.weapons import Wooden_Sword

class Player:
    def __init__(self,
                 name,
                 classType = None, 
                 strength = 5, mana = 5, endurance = 5, intelligence = 5, agility = 5, dexterity = 5, luck = 5, charisma = 5, wisdom = 5, experience = 0, expNeeded = 10, 
                 ):
        self.name = name
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
        self.skills = [{}]
        self.hp = self.calculate_hp()
        self.inventory = {
            "items":{},
            "weapons": {},
            "materials": {},
            "armors":{},
            "quest_items": {},
            }
        self.equipment = {
            "armor": None,
            "weapon": Wooden_Sword(),
            "accessory": None
        }
        self.battle_items = {
            "consumables": {},
        }
        self.classType = classType

    classLookup = {
        'archer': {
            'stat_increase': [
                {
                    "name": "dexterity",
                    "value": 5,
                },
                {
                    "name": "agility",
                    "value": 4,
                }
            ],
        },
        'mage':{
            'stat_increase': [
                {
                    "name": "intelligence",
                    "value": 5,
                },
                {
                    "name": "wisdom",
                    "value": 4,
                }
            ]
        },
        'warrior': {
            "stat_increase": [
                {
                    "name": "strength",
                    "value": 5,
                },
                {
                    "name": "endurance",
                    "value": 4,
                }
            ]
        }
    }

    def calculate_hp(self):
        return self.endurance * 10

    def take_damage(self, amount):
        self.hp -= amount
        print(f"{self.name} takes {amount} damage. HP is now {self.hp}.")

    def level_up(self):
        while self.experience > self.expNeeded:
            self.experience -= self.expNeeded
            self.expNeeded += int(self.expNeeded * 0.25)
            self.level += 1
            if self.level < 5:
                self.stat_points += 5
                print("acquired 5 stat points")
            else:
                self.stat_points += 3
                print("acquired 3 stat points")
        self.hp = self.calculate_hp()
        print("leveled up 1!")
    def show_level(self):
        print(f"leveled up to ${self.level}")

    def gain_experience(self, amount):
        self.experience += amount
        print(f"Gained {amount} XP.")
        if self.experience >= self.expNeeded:
            self.level_up()
    
    def calculate_hit_points(self, classType=None):
        hit_points = 0
        weapon = self.equipment["weapon"].attack
        if classType == 'archer':
            hit_points = (self.agility *0.5) + (self.dexterity*0.5)
        elif classType == "mage":
            hit_points = (self.wisdom*0.5) + (self.intelligence* 0.5)
        elif classType == 'warrior':
            hit_points = (self.strength*0.5) + (self.endurance * 0.5)
        return 1 + (hit_points // 10) + weapon
    
    def calculate_def(self):
       base = (self.endurance* 0.25)
       equip = 0
       if self.equipment["armor"]:
           equip = self.equipment.armor.value // 10
       return base+equip
    
    def add_to_inventory(self, inventory_section: dict, item_name: str):
        print(f"{self.name} acquired {item_name}x1")
        if item_name in inventory_section:
            inventory_section[item_name] += 1
        else:
            inventory_section[item_name] = 1