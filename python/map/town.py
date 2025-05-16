from menus.town_menu import town_menu
from menus.hunter_association_menu import hunter_association_main_menu
from menus.dungeon_menu import dungeon_main_menu
from menus.home_menu import home_menu
from menus.guild_menu import guild_main_menu

def town():
    #town choices
    town_choice = town_menu()
    
    if town_choice == 2:
    #hunter association choices
       hunter_choice = hunter_association_main_menu()
    elif town_choice == 4:
    #going to a dungeon
        dungeon_choice = dungeon_main_menu()
    #OPTIONAL: going to secret dungeon once you get a key
    elif town_choice == 1:
    #going home to sleep (ends the day)
        home_choice = home_menu()
    elif town_choice == 3:
        guild_choice = guild_main_menu()
    #join a guild or create your own need necessary reqs.

    #go into to contract with craftsmen guild need necessary reqs

    #do daily challenges you can do more than max.