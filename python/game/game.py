from player import Player
from town.main import town
from game.time import get_day, get_is_daytime
from intro import center_text

#player
def game():
    #main variables
    day = get_day()
    #Opening Sequence
    name = input("You get teleported to another world what is your name stranger?")
    player = Player(name)
    print(f"Welcome {name} to the world of hunters every choice you make will effect this world and how you navigate it.")
    print(center_text(f"Day {day}"))
    #town
    town()
