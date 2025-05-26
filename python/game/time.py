#day system mechanics 
day = 1
is_daytime = True


def advance_day():
    global day, is_daytime
    day += 1
    is_daytime = True
    
def change_time_of_day():
    global is_daytime
    is_daytime = False

def get_day():
    return day

def get_is_daytime():
    return is_daytime