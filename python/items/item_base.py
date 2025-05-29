class Item:
    def __init__(self, name, description, value=0):
        self.name = name
        self.description = description
        self.value = value
        self.type = "item"

    def use(self):
        print(f"You used {self.name}.")