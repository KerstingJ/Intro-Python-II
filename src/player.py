# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    """Player Object for Adventure Game"""

    actions = ["grab", "inspect", "inventory", "eat"]

    def __init__(self, room):
        self.room = room
        self.health = 100
        self.strength = 10
        self.items = []
        self.message = ""

    def possible_actions(self):
        return ["quit", *Player.actions]

    def describe_room(self):
        """
        prints a description of the current room
        includes room description with name and description
        possible movements, and possible actions
        """
        self.room.display()
        print("\nPossible Actions:")
        print(*self.possible_actions(), sep=", ")

        if len(self.message) > 0:
            print(f"\nLast Action result: \n{self.message}")

    def move(self, move):
        """
        if move is a move available for the players current room
        move player to the room in that direction
        """
        if move in self.room.get_possible_moves():
            self.room = getattr(self.room, f"{move}_to")
            self.message = f"You move to the {self.room.name}"
        else:
            self.message = f"You can move that way"

    def eat(self, item_name):
        items = [item for item in items if item.name == item_name]
        if len(items) > 0 and items[0].consumable == True:
            item = items.pop()
            message = f"\n you ate the {item.name}"
            for key in item.effects:
                attr = getattr(self, key)
                attr += item.effects[key]
                effect = "gained" if item.effects[key] > 0 else "lost"
                message += f"\nyour {key} {effect} points"

        else:
            self.message = f"could not eat item: {item_name}"

    def inspect(self, item_name):
        items = [item for item in self.room.items if item.name == item_name]
        if len(items) > 0:
            self.message = items[0].__str__()
        else:
            self.message = f"could not see item: {item_name}"

    def grab(self, item_name):
        items = [item for item in self.room.items if item.name == item_name]
        if len(items) > 0:
            self.message = items[0].__str__()
        else:
            self.message = f"could not find item: {item_name}"

    def reducer(self, action, item):
        getattr(self, action)(item)
