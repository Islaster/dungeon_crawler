from .weapon_base import Weapon

class Wooden_Sword(Weapon):
    def __init__(self):
        super().__init__("Wooden Sword", "A practice Sword. Very well made", 0, 10, 1)