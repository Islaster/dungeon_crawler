from items.weapons.weapons import Wooden_Sword
from items.registry import item_lookup
from utils.ui import center_text



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
        while self.experience >= self.expNeeded:
            self.experience -= self.expNeeded
            self.expNeeded += int(self.expNeeded * 2)
            self.level += 1
            if self.level < 5:
                self.stat_points += 5
            else:
                self.stat_points += 3
        self.hp = self.calculate_hp()
        print("leveled up 1!")
        print(f"acquired {self.stat_points} stat points")
        self.allocate_stats()
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
        return (hit_points // 10) + weapon + 1
    
    def calculate_def(self):
       base = (self.endurance* 0.2)
       equip = 0
       if self.equipment["armor"]:
           equip = self.equipment.armor.value // 10
       return base+equip
    
    def add_to_inventory(self, inventory_section: dict, item_name: str):
        print(f"{self.name} acquired {item_name}x1")
        if item_name in inventory_section:
            inventory_section[item_name].amount += 1
        else:
            inventory_section[item_name] = {"amount": 1}
    
    def check_for_battle_items(self):
        for item in self.inventory["items"]:
            full_item = item_lookup[item]
            if full_item.item_type == 'consumable':
                if item in self.battle_items:
                    self.battle_items[item]["amount"] += 1
                else:
                    self.battle_items[item] = {"value": full_item, "quantity": 1}

    def allocate_stats(self):
        stat_map = {
            "str": "strength",
            "end": "endurance",
            "int": "intelligence",
            "agi": "agility",
            "dex": "dexterity",
            "lck": "luck",
            "cha": "charisma",
            "wis": "wisdom",
        }

        while self.stat_points > 0:
            print(center_text(f"You have {self.stat_points} stat points left.\n"))
            for code, attr in stat_map.items():
                print(center_text(f"type {code.upper()} to choose {attr}"))

            choice = input("Choose a stat to add points to: ").strip().lower()

            if choice in stat_map:
                try:
                    amount = int(input("How many points do you want to add?\n").strip())
                    if amount > 0 and amount <= self.stat_points:
                        current = getattr(self, stat_map[choice])
                        setattr(self, stat_map[choice], current + amount)
                        self.stat_points -= amount
                        print(f"✅ {amount} points added to {stat_map[choice]}")
                    else:
                        print("Not enough stat points or invalid number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("Invalid stat name.")
