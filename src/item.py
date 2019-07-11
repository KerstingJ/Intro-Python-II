
class Item:
    def __init__(self, name, description, type="normal"):
        self.name = name
        self.description = description
        self.consumable = False
        self.type = type

    @classmethod
    def createConsumable(self, name, description, affects):
        """
        creates a consumable item
        """
        pass

    def __str__(self):
        return f"{self.name}: {self.description}"
