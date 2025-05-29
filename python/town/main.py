from menus.town_menu import town_menu
from utils.town import travel_to

def town():
    global secret_key
    #town choices
    choice = town_menu()
    
    town_choices = {
        #going home to sleep (ends the day)
        1: lambda: travel_to("home"),
        #hunter association choices
        2: lambda: travel_to("hunter association"),
        3: lambda: travel_to("guild"),
        #going to a dungeon
        4: lambda: travel_to("portals")
    }

    action = town_choices.get(choice)
    if action:
        action()
 
    #OPTIONAL: going to secret dungeon once you get a key
    #join a guild or create your own need necessary reqs.

    #go into to contract with craftsmen guild need necessary reqs

    #do daily challenges you can do more than max.