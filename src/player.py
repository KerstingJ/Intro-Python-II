from item import Item
# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    """Player Object for Adventure Game"""

    # TODO: make a help action that looks up action in dictionary and prints details
    actions = ["inspect", "grab", "inventory", "eat", "drop", "destroy"]

    def __init__(self, room, items=None):
        self.room = room
        self.health = 100
        self.strength = 10
        self.items = items or []
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
        if move is a valid move for the players current room
        move player to the room in that direction
        """
        if move in self.room.get_possible_moves():
            self.room = getattr(self.room, f"{move}_to")
            self.message = f"You move to the {self.room.name}"
        else:
            self.message = f"You can not move that way"

    def inspect(self, item_name):
        """ 
        Inspects the item with item_name if it exists in the players
        current room
        """
        item = Item.findByName(item_name, self.room.items)
        if item is not None:
            self.message = item.__str__()
        else:
            self.message = f"could not see item: {item_name}\n found"

    def inventory(self):
        inventory = [item.name for item in self.items]
        items = ", a ".join(inventory)
        self.message = f"in your bag you find:\na {items}"

    def grab(self, item_name):
        """
        grabs item with item_name if it exists in players current room
        """
        # get removed the item from the item array if it is found
        item = Item.getByName(item_name, self.room.items)
        if item is not None:
            self.items.append(item)
            self.message = f"You grab the {item.name} and add it to your inventory"
        else:
            self.message = f"could not find item: {item_name}"

    def eat(self, item_name):
        item = Item.getByName(item_name, self.items)
        if item is not None and item.consumable == True:
            message = f"\n you ate the {item.name}"
            for key in item.effects:
                attr = getattr(self, key)
                attr += item.effects[key]
                effect = "gained" if item.effects[key] > 0 else "lost"
                message += f"\nyour {key} {effect} {item.effects[key]} points"
            self.message = message
        else:
            self.message = f"could not eat item: {item_name}"

    def drop(self, item_name):
        item = Item.getByName(item_name, self.items)
        if item is not None:
            self.room.items.append(item)
            self.message = f"you drop {item.name} on the floor of the {self.room.name}"

    def destroy(self, item_name):
        item = Item.getByName(item_name, self.items)
        if item is not None:
            self.message = f"you stomp the {item.name} into the floor until it cant be distinguished from dust"

    def reducer(self, action, item):
        """
        calls a player objects methods based on the string passed in as action
        and passes that method the string value of item

        """
        getattr(self, action)(item)

    def do(self, next):
        # handle user input

        # If input is an option to move
        if next in self.room.get_possible_moves():
            self.move(next)
        # if input is
        elif next == "inventory":
            self.inventory()
        elif next.split(" ")[0] in self.possible_actions():
            # actions are input as a string "action item"
            verb = next.split(" ")[0]
            noun = next[len(verb)+1:]
            self.reducer(verb, noun)

#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name']
