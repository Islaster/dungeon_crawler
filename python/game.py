from player import Player
from map.floor1 import room_one

#player
player = Player()
def floor1():
    room_one(player)
def game():
    print('opening sequence')
    floor1()
    
    