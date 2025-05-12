from player import Player
from map.floor1 import room_one

#player
player = None
def floor1():
    room_one(player)
def game():
    name = input("You get teleported to another world what is your name stranger?")
    player = Player(name)
    print(f"Welcome ${name} to the world of hunters every choice you make will effect this world and how you navigate it.")
    floor1()
    
    