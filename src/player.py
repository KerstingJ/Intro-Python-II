# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    """Player Object for Adventure Game"""

    def __init__(self, room):
        self.room = room

    def describe_room(self):
        print("\n")
        self.room.display()
        print("What do you want to do?")
        print("Possible Moves: ", self.room.get_moves())
        print("Possible Actions: ", "[None]")

    def move(self, dir):
        """
        if dir is a move available for the players current room
        move player to the room in that direction
        """
        if dir in self.room.get_moves():
            self.room = getattr(self.room, f"{dir}_to")
