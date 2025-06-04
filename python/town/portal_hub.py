from menus.dungeon_menu import dungeon_main_menu, main_dungeons, secret_dungeons
from dungeons.normal import E
from game.game import hero

def portal_hub():
    while True:
        choice = dungeon_main_menu()
        if choice == 1:
            portal_choice = main_dungeons()
            portals = {
               1: E.Rotten_Hollow
            }
            action = portals.get(portal_choice)
            if action:
                action(hero)
                break
        elif choice == 2:
            portal_choice = secret_dungeons()