

def battle(player, enemy):
    turn = 1
    print("Choose your action:")
    choice = input("1.Attack\n2.Items\n3.Skills\n4.Retreat\n")
    
    if choice == 1:
          attack(player, enemy)
    elif choice == 2:
        list(map(lambda pair: print(f"{pair[0]+1}. {pair[1].name} x{pair[1].quantity}\n"), enumerate(player.battle_items)))
    elif choice == 3:
            if len(player.skills)> 0:
                list(map(lambda pair: print(f"{pair[0]+1}. {pair[1].name} x{pair[1].quantity}\n"), enumerate(player.skills)))
            else:
                 input("You have no skills.\nPress enter to go back.")
                 battle(player, enemy)
    elif choice == 4:
         print("tbd")
def attack(player, enemy):
    if player.calculate_hit_points() - enemy.calculate_def() < 0:
        if player.calculate_hit_points() - enemy.equipment.armor.value > 0:
            enemy.equipment.armor.value = player.calculate_hit_points - enemy.equipment.armor.value
        else:
            enemy.equipment.armor.value = 0   
    else:  
       enemy.hp = enemy.hp - (player.calculate_hit_points() - enemy.calculate_def())        


   