def guild_menu():
    global is_in_guild, is_guild_leader
    choice = None
    if is_in_guild and not is_guild_leader:
        choice = input(
            "1. check guild quests\n"
            "2. go to guild store\n"
            "3. check guild status\n"
            "4. check position in guild\n")
    elif is_in_guild and is_guild_leader:
        choice = input(
            "1. assign guild quests\n"
            "2. go to guild store\n"
            "3. check guild status\n"
            "4. manage guild.\n")
    else:
        choice = input(
            "1. Join a Guild\n"
            "2. Create a Guild")
    return choice
    