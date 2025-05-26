from menus.town_menu import town_menu
from .util import travel_to

def town():
    global secret_key
    #town choices
    town_choice = town_menu()
    
    choices = {
        #going home to sleep (ends the day)
        1: travel_to("home"),
        #hunter association choices
        2: travel_to("hunter association"),
        3: travel_to("guild"),
        #going to a dungeon
        4: travel_to("portal hub")
    }

    action = choices.get(town_choice)
    if action:
        action()
 
    #OPTIONAL: going to secret dungeon once you get a key
    #join a guild or create your own need necessary reqs.

    #go into to contract with craftsmen guild need necessary reqs

    #do daily challenges you can do more than max.