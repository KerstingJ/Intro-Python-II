from item import Item
# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    """Player Object for Adventure Game"""

    # TODO: make a help action that looks up action in dictionary and prints details

    def __init__(self, room, items=None, equipment=None):
        self.room = room
        self.health = 100
        self.base_strength = 10
        self.base_defense = 10
        self.strength = 10
        self.defense = 10
        self.items = items or []
        self.equipment = equipment or []
        self.message = ""

    def possible_actions(self):
        # TODO: make this dynamic, possible actions depend on state
        if len(self.items) > 0:
            i_actions = ["eat", "drop", "destroy"]
        else:
            i_actions = []

        # chose this style because it fits nicely on one line
        # while still being readable
        r_actions = [] if len(self.room.items) <= 0 else ["grab"]

        inspect = ["inspect"] if len(
            i_actions) > 0 or len(r_actions) > 0 else []

        equip = []
        for item in self.items:
            if item.item_type == "equipable":
                equip.append("equip")
                break

        return ["quit", "status", "inventory", *inspect, *r_actions, *i_actions, *equip]

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

    def inspect(self, item_name, location="room"):
        """ 
        Inspects the item with item_name if it exists in the players
        current room
        """

        # if user specified location part item_name for location
        # we assume that input will have format
        # "item in location"
        # TODO: this may be able to get pulled out to be used with other commands
        # ex. eat, destroy
        if " in " in item_name:
            # if the item_name contains ` in ` we expect the second half to be a location
            # players can serch `in room` or `in inventory`
            item_name, location = item_name.split(" in ")
        else:
            # if no location specified lets assume they are looking
            # around the room
            item_name = item_name
            location = "room"

        # get item from location
        if location == "room":
            item = Item.findByName(item_name, self.room.items)
        elif location == "inventory":
            item = Item.findByName(item_name, self.items)

        if item is not None:
            self.message = f"{item.__str__()}, {item.item_type}"
        else:
            self.message = f"could not see {item_name} in {location}"

    def inventory(self):
        inventory = [item.name for item in self.items]
        items = ", a ".join(inventory)
        self.message = f"in your bag you find:\na {items}"

    def status(self):
        self.message = f"""
        Player Status:
        health: {self.health}
        strength: {self.strength}
        defense: {self.defense}
        """

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

        if item is not None and item.item_type == "consumable":
            message = f"\n you ate the {item.name}"
            for key in item.effects:
                # get current attributes value
                attr = getattr(self, key)
                # update attribute
                setattr(self, key, attr + item.effects[key])

                # build result message
                effect = "gained" if item.effects[key] > 0 else "lost"
                message += f"\nyou {effect} {abs(item.effects[key])} points of {key}"

            self.message = message
        else:
            if item is not None:
                self.items.append(item)

            self.message = f"could not eat {item_name}"

    def equip(self, item_name):
        item = Item.getByName(item_name, self.items)

        if item is not None and item.item_type == "equipable":
            message = f"\n you equip {item.name}"
            for stat in item.effects:

                base = getattr(self, f"base_{stat}")
                current = getattr(self, stat)

                # set stat to its current value plus the value of the multiplier
                multiplier = (base * item.effects[stat])
                setattr(self, stat, current + multiplier)
            # TODO: make message more informative
            self.message = message
            self.equipment.append(item)
        else:
            if item is not None:
                self.items.append(item)
            self.message = f"could not equip {item.name}"

    def drop(self, item_name):
        item = Item.getByName(item_name, self.items)
        if item is not None:
            self.room.items.append(item)
            self.message = f"you drop {item.name} on the floor of the {self.room.name}"

    def destroy(self, item_name):
        item = Item.getByName(item_name, self.items)
        if item is not None:
            self.message = f"you stomp the {item.name} into the floor until it cant be distinguished from dust"

    def do_with(self, action, item):
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
        elif next == "status":
            self.status()
        elif next.split(" ")[0] in self.possible_actions():
            # actions are input as a string "action item"
            verb = next.split(" ")[0]
            noun = next[len(verb)+1:]
            self.do_with(verb, noun)

#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name']
