from menus.home.home_menu import home_menu
from menus.home.storage_menu import storage_main_menu, item_type_selection_menu, weapon_type_selection_menu, inventory_type_selection_menu
from game.time import advance_day, change_time_of_day, get_day
from intro import center_text
from utils.town import travel_to

storage = {}
def home():
    global storage
    while True:
        home_choice = home_menu()

        if home_choice == 1:
            advance_day()
            day = get_day()
            print(center_text(f"Day {day}"))
            travel_to("town")
            break
        elif home_choice == 2:
            pass
        elif home_choice == 3:
            change_time_of_day()
            print(center_text(f"Night {day}"))
        elif home_choice == "l":
            travel_to("town")
            break
        elif home_choice == 4:
            #menu to get or put items in storage
            storage_choice = storage_main_menu()
            #put away option
            if storage_choice == 1:
               inventory_choice = inventory_type_selection_menu()
               if inventory_choice == 1:
                  item_choice = item_type_selection_menu()

            #take out option
            elif storage_choice == 2:
                inventory_choice = inventory_type_selection_menu()
            #item storage
            storage
        