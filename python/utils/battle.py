import random
from .town import travel_to
from monsters.registry import monster_lookup

def attack(player, enemy):
    calculate_damage = player.calculate_hit_points() - enemy.calculate_def()
    if calculate_damage < 0:
        calculate_damage = 0
    calculate_damage = crit(calculate_damage)
    enemy.hp -= calculate_damage
    print(f"{enemy.name} lost {calculate_damage} has {enemy.hp}hp")

def skill(player, enemy):
    if len(player.skills) < 1:
        print("You have no skills.\n")
        choice = input("press B to go back.")

def items(player, enemy):
    while True:
        lookup = {}
        if len(player.battle_items) < 1:
            print("You have no skills.\n")
            main_choice = input("press B to go back.\n").strip().lower()
            if main_choice == "b":
                return
        for index, (key, value) in enumerate(player.battle_items["consumables"].items(), start=1):
            print(f"Press {index} to look at {key}\n")
            lookup[str(index)] = key
        print("press B to go back\n")
        choice = input("please choose one of the options\n").strip().lower()
        if choice in lookup:
            item = player.battle_items["consumables"][lookup[choice]]
            item["value"].show_stats()
        elif choice == "b":
            return
        use_item = input("press y to use item\n press n to go back\n").strip().lower()
        if use_item == "y":
            item["value"].use(player)
            return
        elif use_item == "n":
            continue
    

    
def retreat(player, enemy, chance=0.65,) -> bool:
    phrases = monster_lookup

    agi = player.agility
    dex = player.dexterity
    lck = player.luck
    
    mon_agi = enemy.agility
    mon_dex = enemy.dexterity
    mon_lck = enemy.luck

    player_chance = (agi + dex + lck) - (mon_agi + mon_dex + mon_lck)
    if player_chance < 0:
        print("you failed to get away.")
        return False
    else:
        player_chance /= 100
        chance += player_chance
        if random.random() <= chance:
            print(phrases[enemy.name]["escape"])
            travel_to("town")
            return
        else:
            print(phrases[enemy.name]["escape_fail"])
            return

def crit(damage):
    if random.random() <= .10:
       return (damage * 2)
    else: 
        return damage

