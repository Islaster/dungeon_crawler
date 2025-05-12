from .monster import Monster
from items.materials import Slime_Core, Slime_Residue, Goblin_Ear
from items.items import Stolen_Coin_Purse

slime = Monster("Slime",3, 5, 5, 1, 2, 1, 0, 0, 10, {
    "materials": [Slime_Core(), Slime_Residue()],
    "exp": 2,
    "gold": 5,
    }, None, None)

goblin = Monster("Goblin", 3, 0, 3, 1, 5, 3, 0, 0, 15, {
"materials": [Goblin_Ear(), Stolen_Coin_Purse()],
"exp": 2,
"gold": 5,
}, {}, None )