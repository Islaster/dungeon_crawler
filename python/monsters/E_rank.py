from .monster import Monster
from items.items import Moldy_Wine
from items.materials import Gremlin_tooth, Rat_fang, Broodmother_Wing

gremlin = Monster(
    "speed",#type
    "Mold Gremlin",#name
    3,#strength 
    0,#mana 
    2,#endurance 
    1,#intelligence 
    3,#agility
    2,#dexterity 
    1,#luck 
    0,#wisdom
    {"xp": 10, "items": [Moldy_Wine(), Gremlin_tooth()]}#drops
)

rat_alpha = Monster(
    "strength",#type
    name="Spore Rat Alpha",#name
    strength=5,#strength 
    mana=0,#mana
    endurance=4,#endurance 
    intelligence=1,#intelligence 
    agility=4,#agility
    dexterity=3,#dexterity 
    luck=2,#luck 
    wisdom=1,#wisdom 
    drops={"xp": 25, "items": [Rat_fang()]}#drops
)

broodmother = Monster(
    "strength",#type
    "Carrionfly Broodmother",#name
    7,#strength
    0,#mana 
    5,#endurance
    3,#intelligence 
    5,#agility
    3,#dexterity 
    2,#luck 
    2,#wisdom
    {"xp": 50, "items": [Broodmother_Wing()]}#drops
)