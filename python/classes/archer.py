from player import Player
import random

def calculate_hit(attacker_dexterity, attacker_luck, target_agility):
    base_hit_chance = 70  # baseline chance in %
    
    # Dexterity adds directly to hit
    hit_bonus = attacker_dexterity * 1.5

    # Luck gives slight chance boost
    luck_bonus = attacker_luck * 0.5

    # Target agility reduces hit chance
    evasion_penalty = target_agility * 1.2

    final_chance = base_hit_chance + hit_bonus + luck_bonus - evasion_penalty
    final_chance = max(5, min(95, final_chance))  # clamp between 5% and 95%
    
    roll = random.randint(1, 100)
    print(f"Hit chance: {final_chance:.2f}%, Roll: {roll}")

    return roll <= final_chance


class Archer(Player):
    super.__init__(
        self,
        strength=6,
        mana=3,
        endurance=6,
        intelligence=5,
        agility=9,
        dexterity=12,
        luck=8,
        charisma=4,
        wisdom=4
        )
    def basic_attack(self, target_agility):
        hit = calculate_hit(self.dexterity,self.luck, target_agility)
        print("You shot your bow")
        if hit:
            return self.attack
    def precision_shot(self):
        print(f"You fire a precision shot with dexterity")

    def calculate_hit_points(self):
        hit_points = 1
        increase = (self.agility * 0.5) + (self.dexterity * 0.5)
        hit_points += (increase // 10)