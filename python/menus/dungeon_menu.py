def dungeon_main_menu():
    choice = input(
        "1. Enter dungeon\n"
        "2. Enter secret dungeon\n"
        )
    return int(choice)

def main_dungeons():
    choice = input(
        "1. E-rank dungeon\n"
        "2. D-rank dungeon\n"
        "3. C-rank dungeon\n"
        "4. B-rank dungeon\n"
        "5. A-rank dungeon\n"
        "6. S-rank dungeon\n"
        )
    return int(choice)

def secret_dungeons():
    choice = input(
        "1. E-rank dungeons\n"
        "2. D-rank dungeons\n"
        "3. C-rank dungeons\n"
        "4. B-rank dungeons\n"
        "5. A-rank dungeons\n"
        "6. S-rank dungeons\n"
    )
    return int(choice)