import textwrap
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Lav", room['outside'])

# Write a loop that:
while True:
    print("=====================\n")

    # * Prints the current room name
    print(f"Location: {player.current_room.name}")

# * Prints the current description (the textwrap module might be useful here).
    for line in textwrap.wrap(player.current_room.print_desc()):
        print(line)

    # If the user enters "q", quit the game.
    print("Press q to exit game")

# * Waits for user input and decides what to do.
    choice = input("Choose Direction(n, w, e, s): ").lower().strip()
# If the user enters a cardinal direction, attempt to move to the room there.
    if choice in ["q", "quit", "exit"]:
        break
    if choice in ["n", "w", "e", "s"]:
        player.current_room = player.move(choice, player.current_room)
# Print an error message if the movement isn't allowed.
    else:
        print("Please enter a valid direction")
