def main_menu():
    choice = input(
            "\n=== DGN ===\n"
            "Press S to Start Game\n"
            "Press L to Load Game\n"
            "Press E to Exit\n"
        ).strip().lower()
    return choice