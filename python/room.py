import random

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
        print(f"\n⚠️ Trap triggered: {self.trap['description']}")
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
        enemy = self.enemy.copy()
        print(f"\n⚔️ {enemy['name']} appears!")

        while enemy["hp"] > 0 and player.hp > 0:
            # Player attacks
            base_damage = player.calculate_hit_points(player.classType)
            dmg = random.randint(5, 10) + base_damage
            enemy["hp"] -= dmg
            print(f"You hit {enemy['name']} for {dmg} → Enemy HP: {max(0, enemy['hp'])}")

            if enemy["hp"] <= 0:
                print(f"✅ You defeated {enemy['name']}!")
                player.gain_experience(enemy["xp"])
                return

            # Enemy attacks
            edmg = random.randint(enemy["atk_min"], enemy["atk_max"])
            reduced_dmg = int(edmg - player.calculate_def())
            reduced_dmg = max(reduced_dmg, 1)  # Minimum 1 dmg
            player.take_damage(reduced_dmg)

            if player.hp <= 0:
                print("💀 You died...")
                exit()

    def handle_reward(self, player):
        item = self.reward["item"]
        effect = self.reward["effect"]
        rtype = self.reward["type"]
        print(f"\n🎁 You found {item} (+{effect} {rtype})")

        if rtype == "hp":
            player.hp += effect
            print(f"{player.name}'s HP restored to {player.hp}")
        elif rtype == "xp":
            player.gain_experience(effect)

        player.inventory.append(item)
