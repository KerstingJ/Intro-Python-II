
class Item:
    def __init__(self, name, description, item_type="normal"):
        """
        creates a consumable item
        takes in a name, description, and option item_type
        """
        self.name = name
        self.description = description
        # TODO: refactor to use item_type insted of boolean consumable
        self.item_type = item_type
        self.consumable = False
        self.effects = None

    @classmethod
    def create_consumable(cls, name, description, effects):
        """
        creates a consumable item
        takes in a name, description, item_type, and effects
        effects expects a dictionary
            key being the name of the player stat it affects
            value being an integer value to be applied to that stat
        """
        item = cls(name, description, "consumable")
        item.consumable = True
        item.effects = effects
        return item

    # TODO Create equipable factory
    @classmethod
    def create_equipable(cls, name, description, effects):
        """
        creates an equipable item
        takes in a name, description, and effects
        effects expects a dictionary
            key being the name of the player stat it affects
            value being an integer value to be applied to that stat
        """
        item = cls(name, description, "equipable")
        item.consumable = false
        item.effects = effects
        return item

    @staticmethod
    def findByName(name, item_list):
        """ 
        find an Item in a list of items by name
        return the item
        if no matching item is found returns None
        """
        for item in item_list:
            if item.name == name:
                return item

        return None

    @staticmethod
    def getByName(name, item_list):
        """ 
        find an Item in a list of items by name
        remove and returns the item
        if no matching item is found returns None
        """
        for i in range(len(item_list)):
            if item_list[i].name == name:
                return item_list.pop(i)

        return None

    def __str__(self):
        return f"{self.name}: {self.description}"
