from player import Player
from map.floor1 import room_one

#day system mechanics 
day = 1
is_sleep = False
is_daytime = True
is_resting = False

def advance_day():
    global day, is_sleep, is_daytime
    if is_sleep == True:
        day += 1
        is_daytime = True
    
def change_time_of_day():
    global is_daytime, is_resting
    if is_resting == True:
        is_daytime = False

#player
player = None
def game():
    global player
    
    #Opening Sequence
    name = input("You get teleported to another world what is your name stranger?")
    player = Player(name)
    print(f"Welcome ${name} to the world of hunters every choice you make will effect this world and how you navigate it.")
    
    #town
    
