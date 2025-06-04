from .material_base import Material

class Gremlin_tooth(Material):
    def __init__(self):
        super().__init__("Gremlin Tooth", "A sharp fang from a Mold Gremlin.", ["Goblin Tooth"])

class Rat_fang(Material):
    def __init__(self):
        super().__init__("Rat Fang", "Trophy from defeating a large rat.")

class Broodmother_Wing(Material):
    def __init__(self):
        super().__init__("Broodmother Wing", "Buzzes faintly with dark energy.")
