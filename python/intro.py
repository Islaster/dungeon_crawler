import os
import time
import sys
from pyfiglet import Figlet
import shutil
import termios
import tty
import sys
import select

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def center_text(text: str) -> str:
    terminal_width = shutil.get_terminal_size().columns
    lines = text.splitlines()
    return '\n'.join(' ' * max((terminal_width - len(line)) // 2, 0) + line for line in lines)

def is_key_pressed():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    tty.setcbreak(fd)

    rlist, _, _ = select.select([fd], [], [], 0)
    if rlist:
        sys.stdin.read(1)  # ✅ consume the key so it's not checked again
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
        return True

    termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return False


def print_dgn_ascii():
    f = Figlet(font='slant')  # You can try 'doom', 'big', 'banner3-D', etc.
    print(center_text(f.renderText('D G N')))

def show_intro():
    clear_screen()
    print_dgn_ascii()
    time.sleep(2)

    clear_screen()
    print_dgn_ascii()
    print("\n" + center_text(">> PRESS ENTER TO START <<"))
    input()  # Just wait for Enter
    clear_screen()

