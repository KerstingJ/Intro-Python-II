
class Item:
    def __init__(self, name, description, item_type="normal"):
        """
        creates a consumable item
        takes in a name, description, and option item_type
        """
        self.name = name
        self.description = description
        self.item_type = item_type
        self.consumable = False
        self.effects = None

    @classmethod
    def create_consumable(cls, name, description, item_type, effects):
        """
        creates a consumable item
        takes in a name, description, item_type, and effects
        effects expects a dictionary
            key being the name of the player stat it affects
            value being an integer value to be applied to that stat
        """
        item = cls(name, description, item_type)
        item.consumable = True
        item.effects = effects
        return item

    def __str__(self):
        return f"{self.name}: {self.description}"
