from .item_base import Item

class Material(Item):
    def __init__(self, name, description, combinable_with=None):
        super().__init__(name, description, value=0)
        self.type = "material"
        self.combinable_with = combinable_with or []

    def can_combine_with(self, other_material):
        return other_material.name in self.combinable_with