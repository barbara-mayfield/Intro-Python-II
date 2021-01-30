import textwrap
import os
import sys
import time
from room import Room
from player import Player, Profession
from item import Item, Weapon

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

# declare items

coin = Item("coin", "How did this get here?")
torch = Item("torch", "A stick with a flame on the end")
stick = Weapon("stick", "Its a stick...", "Mid", 2)
sword = Weapon("sword", "A long sharp blade.", "Mid", 4)

# assign items to rooms

room['outside'].add_item(coin)
room['outside'].add_item(stick)

room['foyer'].add_item(stick)
room['foyer'].add_item(sword)

# create professions
rogue = Profession("warrior")
druid = Profession("rogue")
necromancer = Profession("druid")


#
# Main
#

def title_screen_select():
    option = input(">> ").lower()

    if option == "play":
        setup_game()
    elif option == "help":
        help_menu()
    elif option == "quit":
        player.game_over = True
    while option not in ("play", "help", "quit"):
        f"Please enter a valid command."
        option = input(">> ")
        continue


def title_screen():
    os.system("clear")
    print("############################")
    print("# Welcome to the Text RPG! #")
    print("############################")
    print("          - Play -          ")
    print("          - Help -          ")
    print("          - Quit -          ")
    title_screen_select()


def help_menu():
    print("############################")
    print("# Welcome to the Text RPG! #")
    print("############################")
    print("- Use up, down, left, right to move -")
    print("- Use 'look' to inspect something   -")
    print("-       Good Luck & Have Fun        -")
    title_screen_select()


# Make a new player object that is currently in the 'outside' room.
player = Player("Lav", 100, room['outside'])

# Write a loop that:


def main_game_loop():
    while player.game_over == False:
        # * Prints the current room name
        print(f"\nLocation: {player.current_room.name}")

        # * Prints the current description (the textwrap module might be useful here).
        for line in textwrap.wrap(player.current_room.print_desc()):
            print(line)
        # * Waits for user input and decides what to do.
        print("\n" + "============================")
        print("What would you like to do?")
        print("h for help or q for quit")
        # * Split the entered command and see if it has 1 or 2 words in it
        try:
            action = input(">> ").lower().strip().split()
        # If the user enters a cardinal direction, attempt to move to the room there.
            if action[0] in ["n", "w", "e", "s"]:
                player.current_room = player.move(
                    action[0], player.current_room)
                print(f"You move to {player.current_room.name}...")
            elif action[0] in ["h", "help"]:
                print("Enter n, w, e, s to move in a direction")
                print("Enter 'get [ITEM]' to prompt an item pickup")
                print("Enter: 'drop [ITEM]' to prompt to drop item")
            elif action[0] == "look":
                print(
                    f"You found {player.current_room.items} in this location.")
            elif action[0] in ["i", "inventory"]:
                print(f"Inventory: {player.inventory}")
                if player.inventory == []:
                    print(f"There is currently nothing in your inventory.")
        # * Implement support for the verb `get` followed by an item name.
            elif action[0] == "get":
                item = action[1]
                player.get_item(item)
            elif action[0] == "drop":
                item = action[1]
                player.drop_item(item)
            elif action[0] in ["q", "quit", "exit"]:
                player.game_over = True
                sys.exit()
            else:
                print("Please enter a valid action")
        except:
            return f"Something went wrong..."


def setup_game():
    os.system("clear")

    # NAME COLLECTING
    question1 = "Hello, whats your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input(">> ")
    player.name = player_name

    # PROFESSION SELECTION
    question2 = f"Hello, {player.name} what role do you want to play?\n"
    question2added = "You can play as a warrior, rogue, or druid.\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input(">> ").lower()
    valid_job = ['warrior', 'rogue', 'druid']
    if player_job in valid_job:
        player.profession = player_job
        print(f"You are now a {player.profession}")
        os.system("clear")
    else:
        print(f"Invalid profession name")

    # INTRODUCTION TO GAME START
    speech1 = f"Welcome {player.name} the {player.profession} to this fantasy world! \n"
    speech2 = "Can you find all it's hidden wonders? \n"
    speech3 = "Just make sure you don't get too lost... \n"
    speech4 = "Bwahahahaha... \n"

    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.10)

    os.system("clear")
    print("############################")
    print("#     Let's Start Now!     #")
    print("############################")
    main_game_loop()


title_screen()
