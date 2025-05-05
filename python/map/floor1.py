from room import Room
from classes.archer import Archer
from classes.mage import Mage
from classes.warrior import Warrior


monster_room = Room("Monster Room", "room filled with monsters", "monster", False,{
        
    })
def room_one(player):
    class_room = Room("Class Room", "room where you choose your class", "unique", False, {
        "c": {
            "a":Archer(),
            "m":Mage(),
            "w": Warrior()
        },
        "w": Room.link_next(monster_room)
    })

def room_two():
    