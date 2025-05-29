from menus.home_menu import home_menu
from game.time import advance_day, change_time_of_day, get_day
from intro import center_text
from utils.town import travel_to


def home():
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
        