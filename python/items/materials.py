from .material_base import Material

class Slime_Core(Material):
    def __init__(self):
        super().__init__("Slime Core", "used for potion and magic tool creation", ["Redleaf", "Iron Ore", "Magic Dust"])

class Redleaf(Material):
    def __init__(self):
        super().__init__("Redleaf", "used for potion and poison creation", ["Slime_Core", "Wormwood"])

class Slime_Residue(Material):
    def __init__(self):
        super().__init__("Slime Residue", "used for potion creation.", ["Blue Petal"])

class Blue_Petal(Material):
    def __init__(self):
        super().__init__("Blue Petal", "used for potion creation", ["Slime Residue"])

class Goblin_Ear(Material):
    def __init__(self):
        super().__init__("Goblin Ear", "bounty trophy and guild proof", None)
