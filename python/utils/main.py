import select
import sys
import termios
import tty

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