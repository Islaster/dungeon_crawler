import random

def attack(player, enemy):
    print(f"player calc hit points: {player.calculate_hit_points()}")
    print(f"enemy def calc: {enemy.calculate_def()}")
    calculate_damage = player.calculate_hit_points() - enemy.calculate_def()
    if calculate_damage < 0:
        calculate_damage = 0
    enemy.hp -= calculate_damage
    print(f"{enemy.name} lost {calculate_damage} has {enemy.hp}hp")

def skill(player, enemy):
    if len(player.skills) < 1:
        print("You have no skills.\n")
        choice = input("press B to go back.")

def items(player, enemy):
    if len(player.battle_items) < 1:
        print("You have no skills.\n")
        choice = input("press B to go back.")
    
def retreat(player, enemy, chance=0.65) -> bool:
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
        chance += (player_chance*0.3)
        if random.random() <= chance:
            return True
        else:
            return False

