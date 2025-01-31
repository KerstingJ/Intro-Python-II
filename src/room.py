# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    """Room object has a name and text"""
    possible_moves = ["n_to", "s_to", "e_to", "w_to"]

    def __init__(self, name, text, items=None):
        self.name = name
        self.text = text
        if items is None:
            self.items = []
        else:
            self.items = items[:]

        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def get_possible_moves(self):
        """
        uses the static list possible moves to generate a list of directions available from a room
        """
        return [mov[:1] for mov in Room.possible_moves if getattr(self, mov) is not None]

    def display(self):
        print(
            f"""{self.name}
            \n   {self.text}""")
        if len(self.items) > 0:
            print("\nYou see some items nearby: ")
            print(*[item.name for item in self.items], sep=", ")
        print("\nPossible Moves: ")
        print(*self.get_possible_moves(), sep=", ")
