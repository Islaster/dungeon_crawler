from room import Room
from classes.archer import Archer
from classes.mage import Mage
from classes.warrior import Warrior



def roomOne():
    monster_room = Room("Monster Room")
    class_room = Room("Class Room", "room where you choose your class", "unique", False, {
        "c": {
            "a":Archer(),
            "m":Mage(),
            "w": Warrior()
        },
        "w": Room.link_next()
    })