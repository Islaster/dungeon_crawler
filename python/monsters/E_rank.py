from .monster import Monster
from items.items import Moldy_Wine
from items.materials import Gremlin_tooth, Rat_fang, Broodmother_Wing

gremlin = Monster(
    name="Mold Gremlin",
    strength=3, mana=0, endurance=2, intelligence=1, agility=3,
    dexterity=2, luck=1, wisdom=0, health_points=20,
    drops={"xp": 10, "items": [Moldy_Wine(), Gremlin_tooth()]}
)

rat_alpha = Monster(
    name="Spore Rat Alpha",
    strength=5, mana=0, endurance=4, intelligence=1, agility=4,
    dexterity=3, luck=2, wisdom=1, health_points=35,
    drops={"xp": 25, "items": [Rat_fang()]}
)

broodmother = Monster(
    name="Carrionfly Broodmother",
    strength=7, mana=0, endurance=5, intelligence=3, agility=5,
    dexterity=3, luck=2, wisdom=2, health_points=50,
    drops={"xp": 50, "items": [Broodmother_Wing()]}
)