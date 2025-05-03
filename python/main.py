from intro import show_intro
from main_menu import main_menu
from exit import exit_game
from game import game
from save import load_game

def main():
    show_intro()
    choice = main_menu()
    choices = {
        's': game,
        'l': load_game,
        'e': exit_game
    }
    action = choices.get(choice)
    if action:
        action()
    else:
        print("Choose a valid option!!")
if __name__ == "__main__":
    main()