from game.time import get_is_daytime


def home_menu():
    is_daytime = get_is_daytime()
    choice = 0

    if is_daytime:
        choice = input("1. Sleep\n"
                   "2. Train\n"
                   "3. Rest\n"
                   "l. leave house"
                   )
    else:
        choice = input("1. Sleep\n"
                   "2. Train\n"
                   "l. leave house"
                   )
    if int(choice):  
        return int(choice)
    else:
        return choice