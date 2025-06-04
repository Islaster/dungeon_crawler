from game.game import hero

def storage_main_menu():
    choice = input(
        "1. Put items in storage\n"
        "2. Retrive items from storage\n"
        )
    return int(choice)

def inventory_type_selection_menu():
    choice = input(
        "1. items\n"
        "2. materials\n"
        "3. weapons\n"
        "4. armors\n"
        )
    return int(choice)

def item_type_selection_menu():
    choice = input("1. consumables\n")
    return int(choice)

def weapon_type_selection_menu():
    choice = input("1. swords\n")
    return int(choice)