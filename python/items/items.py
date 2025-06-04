from .item_base import Item
from utils.ui import center_text

class Moldy_Wine(Item):
    def __init__(self):
        super().__init__("Moldy Wine Flask", "A questionable bottle of healing wine.", 5)
        self.item_type = "consumable"

    def show_stats(self):
        print(center_text(self.name))
        print(center_text(self.description))
        print(center_text(f"restores {self.value} hp"))
    
    def use(self, player):
        player.hp += 5
        print(f"You used {self.name}.")
        