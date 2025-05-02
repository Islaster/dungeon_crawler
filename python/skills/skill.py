class Skill:
    def __init__(self, name, description, allowed_classes, cost=0):
        self.name = name
        self.description = description
        self.allowed_classes = allowed_classes  # List of class names
        self.cost = cost  # Optional mana/stamina cost

    def can_use(self, player):
        return player.__class__.__name__ in self.allowed_classes
