import shutil
import os
from pyfiglet import Figlet

#text
def center_text(text: str) -> str:
    terminal_width = shutil.get_terminal_size().columns
    lines = text.splitlines()
    return '\n'.join(' ' * max((terminal_width - len(line)) // 2, 0) + line for line in lines)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_dgn_ascii():
    f = Figlet(font='slant')  # You can try 'doom', 'big', 'banner3-D', etc.
    print(center_text(f.renderText('D G N')))

def get_grid(obj: dict, rows=4, cols=2):
    total_cells = rows * cols
    #5 skills per page and an extra page for the leftover skills that add up to 5
    pages = []
    #Each page
    index = 0
    skills_index = len(obj)

    for r in range(rows):
        row = []
        for c in range(cols):
            if index < len(grid) and index < skills_index:
                row.append(str(f"{obj}"))
            else:
                row.append(" ")
            index += 1
        print(" | ".join(row))

def get_page(player):
    skills = player.skills
    