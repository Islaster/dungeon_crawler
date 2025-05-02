class Room:
    def __init__(self, name, description, room_type, is_cleared=False):
        self.name = name
        self.description = description
        self.room_type = room_type
        self.is_cleared = is_cleared
        self.next_room = None  # one-way link

    def link_next(self, next_room):
        self.next_room = next_room

    def enter(self, player):
        print(f"{player.name} enters the {self.name}.")
        print(self.description)
