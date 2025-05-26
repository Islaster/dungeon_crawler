from menus.dungeon_menu import dungeon_main_menu, main_dungeons, secret_dungeons

def portal_hub():
    while True:
        choice = dungeon_main_menu()
        if choice == 1:
            portal_choice = main_dungeons()
        elif choice == 2:
            portal_choice = secret_dungeons()