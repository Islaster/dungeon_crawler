from room import Room
from monsters.E_rank import broodmother, gremlin, rat_alpha
def Rotten_Hollow(player):
   print("\n🌀 A green portal appears in the outskirts of town...")
   print("You step inside the E-Rank Dungeon: Rotten Hollow.")

   rooms = [
      Room("Moldy Storage Room", "Rotting barrels line the walls.", gremlin),
      Room("Collapsed Hallway", "A thick mist of spores fills the air.",None,{"description": "Poison Spores", "damage": 10, "chance_to_fail": 0.5}),
       Room("Feeding Grounds", "Rats scurry in the shadows.",rat_alpha),
       Room("Broodmother’s Nest", "The air buzzes with insect wings.",broodmother)
   ]

   for room in rooms:
        room.enter(player)

   print("\n🏁 Dungeon Cleared!")
   print(f"HP: {player.hp} | XP: {player.experience} | Inventory: {player.inventory}") 