import random
from utils.ui import center_text
from utils.battle import attack, skill, items, retreat
from menus.battle_menu import main_battle_menu

class Room:
    def __init__(self, name, description, enemy=None, trap=None, reward=None):
        self.name = name
        self.description = description
        self.enemy = enemy
        self.trap = trap
        self.reward = reward

    def enter(self, player):
        print(f"\n📍 {self.name}")
        print(self.description)

        if self.trap:
            self.handle_trap(player)

        if self.enemy:
            self.handle_combat(player)

        if self.reward:
            self.handle_reward(player)

    def handle_trap(self, player):
        print(f"\nTrap triggered: {self.trap['description']}")
        success = random.random() > self.trap.get("chance_to_fail", 0.5)
        if success:
            print("🛡️ You avoided the trap!")
        else:
            damage = self.trap["damage"]
            player.take_damage(damage)
            if player.hp <= 0:
                print("💀 You died...")
                exit()

    def handle_combat(self, player):
        print(f"\n{self.enemy.name} appears!")
        player.check_for_battle_items()
        while self.enemy.hp > 0 and player.hp > 0:
            choice = main_battle_menu()
            # Player choices
            choices = {
                1: attack,
                2: skill,
                3: items,
                4: retreat
            }
            action = choices.get(choice)
            if action:
                action(player,self.enemy)
            else:
                print("pick a valid option")
            
            # Enemy attacks
            if self.enemy.hp > 0:
                edmg = self.enemy.calculate_hit_points()
                print(f"enemy attack does {edmg}")
                reduced_dmg = int(edmg - player.calculate_def())
                player.take_damage(reduced_dmg)

            if player.hp <= 0:
                print(center_text("GAME OVER!!!\nYou died..."))
                exit()
            if self.enemy.hp <= 0:
                print(center_text("You Win."))
                if self.enemy.drops["xp"]:
                    player.gain_experience(self.enemy.drops["xp"])
                if self.enemy.drops["items"]:
                    lookup = {
                        "item": {
                            "bool":True,
                            "value":player.inventory['items']
                            },
                        "material": {
                            "bool": True,
                            "value":player.inventory["materials"]
                            },
                    }
                    for item in self.enemy.drops["items"]:
                        if lookup[item.type]["bool"]:
                            player.add_to_inventory(lookup[item.type]["value"], item.name)
    def handle_reward(self, player):
        item = self.reward["item"]
        effect = self.reward["effect"]
        rtype = self.reward["type"]
        print(f"\nYou found {item} (+{effect} {rtype})")

        if rtype == "hp":
            player.hp += effect
            print(f"{player.name}'s HP restored to {player.hp}")
        elif rtype == "xp":
            player.gain_experience(effect)
