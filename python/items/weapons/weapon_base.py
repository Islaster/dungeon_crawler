class Weapon:
    def __init__(self, name, description,value, durability, attack):
        self.name = name
        self.description = description
        self.value = value
        self.durability = durability
        self.attack = attack
        
        def multiplier(stat):
            self.attack += stat *0.3