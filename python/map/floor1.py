from room import Room
from monsters.lvl1 import slime

from utilFun import battle

def room_one(player):
    monster_room = Room("Monster Room", "room filled with monsters", "monster", False,{
        battle:battle(player, slime),
        
    })
    