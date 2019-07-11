# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    """Player Object for Adventure Game"""

    def __init__(self, room):
        self.room = room

    def describe_room(self):
        """
        Player logs a description of the current room they are in
        includes room description with name and description
        possible movements, and possible actions
        """
        self.room.display()

    def move(self, move):
        """
        if move is a move available for the players current room
        move player to the room in that direction
        """
        if move in self.room.get_possible_moves():
            self.room = getattr(self.room, f"{move}_to")

    def action(self, action):
        pass
