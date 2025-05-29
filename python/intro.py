import time
from utils.ui import center_text, clear_screen, print_dgn_ascii

def show_intro():
    clear_screen()
    print_dgn_ascii()
    time.sleep(2)

    clear_screen()
    print_dgn_ascii()
    print("\n" + center_text(">> PRESS ENTER TO START <<"))
    input()  # Just wait for Enter
    clear_screen()

