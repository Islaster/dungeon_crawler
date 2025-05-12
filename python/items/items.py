from .item_base import Item
import random

class Stolen_Coin_Purse(Item):
    def __init__(self):
        self.gold_amount = random.randint(5, 10)
        super().__init__("Stolen Coin Purse", "stolen from an adventurer maybe?", self.gold_amount)

