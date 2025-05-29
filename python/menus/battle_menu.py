def main_battle_menu():
    choice = input(
        "1. Attack\n"
        "2. Skills\n"
        "3. Items\n"
        "4. Retreat\n"
        )
    if choice.isdigit():
        return int(choice)
    else:
        print("❌ Invalid input. Please enter a number between 1 and 4.")
