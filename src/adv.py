import os
from room import Room
from player import Player
from item import Item
# Declare all the rooms

items = {
    "sandwich": Item.create_consumable(
        "sandwich",
        "a suspiciously fresh sandwich",
        {"health": 50}
    ),
    "old fish": Item.create_consumable(
        "bad fish",
        "yuck, that stinks",
        {"health": -50}
    ),
    "small rock": Item(
        "small rock",
        "a small rock, looks like it would be good to skip across a lake"

    ),
    "garbage": Item(
        "garbage",
        "just some useless garbage"
    )
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [items["garbage"]]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                     [items["small rock"], items["old fish"]]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     [items["old fish"]]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     [items["small rock"], items["sandwich"]]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Visual Map
"""  ___
    | | |
    |  _|
    |_|
"""

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
player = Player(room["outside"], [items["sandwich"], items["sandwich"]])
while True:
    # clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

    # print the room description
    player.describe_room()

    # get user input
    next_action = input("\nWhat will you do? ").strip()

    if next_action == "quit":
        break

    player.do(next_action)
