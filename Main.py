from Room import Room
from Items import Item
from Character import Enemy
from Character import Player
import random

print("Welcome to the haunted house!")
print("\nHow to play:")
print("-Navigate through the rooms, pick up items and kill enemies.")
print("-When you enter a room, the room will be displayed. A door is shown as a '/'.")
print("-In the room, an item is shown as 'i' and an enemy is shown as 'e'.")
print("-Each enemy has a unique weakness item that you need to find, then fight them with.")
print("-If you kill all of the enemies in the house, you win.")
print("-If you lose all 3 of your lives, you lose.")
print("-If you need a list of commands you can use, type 'help'.")
print("\nGood luck!")
input("\n\tPress 'Enter' to continue")

char_name = input("\nWhat would you like to be called?: ")
player_char = Player(char_name)
# print("What do you look like?: ")
# looks = input("> ")
# player_char.set_appearance(looks)

# Rooms
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")

ballroom = Room("Ballroom")
ballroom.set_description("A luxurious looking room before it rotted away")

dining_hall = Room("Dining Hall")
dining_hall.set_description("Where the most posh meals were held")

library = Room("Library")
library.set_description("A room filled with dusty books and cobwebs on the shelves")

laboratory = Room("Laboratory")
laboratory.set_description("An old fashioned laboratory containing strange equipment")

dungeon = Room("Dungeon")
dungeon.set_description("A dark cell where prisoners were kept. ")

bedroom = Room("Bedroom")
bedroom.set_description("A dusty room, filled with cobwebs with a messy, yet somehow neatly made bed")

graveyard = Room("Graveyard")
graveyard.set_description("Cold, misty air surrounding many old, dirty tombstones.")

torture_chamber = Room("Torture chamber")
torture_chamber.set_description("Dried blood splattered on the floor and walls alongside gruesome torture equipment")

# From kitchen
kitchen.link_Room(dining_hall, "south")
kitchen.link_Room(laboratory, "west")

# From Dining Hall
dining_hall.link_Room(kitchen, "north")
dining_hall.link_Room(ballroom, "west")
dining_hall.link_Room(bedroom, "south")

# From Laboratory
laboratory.link_Room(kitchen, "east")
laboratory.link_Room(ballroom, "south")
laboratory.link_Room(graveyard, "west")

# From ballroom
ballroom.link_Room(laboratory, "north")
ballroom.link_Room(dining_hall, "east")
ballroom.link_Room(library, "south")
ballroom.link_Room(dungeon, "west")

# From library
library.link_Room(ballroom, "north")
library.link_Room(bedroom, "east")
library.link_Room(torture_chamber, "west")

# From dungeon
dungeon.link_Room(ballroom, "east")
dungeon.link_Room(graveyard, "north")
dungeon.link_Room(torture_chamber, "south")

# From bedroom
bedroom.link_Room(dining_hall, "north")
bedroom.link_Room(library, "west")

# From graveyard
graveyard.link_Room(laboratory, "east")
graveyard.link_Room(dungeon, "south")

# From torture chamber
torture_chamber.link_Room(dungeon, "north")
torture_chamber.link_Room(library, "east")

rooms = []

rooms.append(kitchen)
rooms.append(dining_hall)
rooms.append(ballroom)
rooms.append(laboratory)
rooms.append(library)
rooms.append(dungeon)
rooms.append(bedroom)
rooms.append(graveyard)
rooms.append(torture_chamber)

# Item names/descriptions
items = []
for i in range(10):
    items.append(Item())

def room_item_setter(item):
    random.shuffle(rooms)
    for x in rooms:        
        if x.item == None:
            x.set_item(item)
            break
        else:
            x = None

for item in items:
    room_item_setter(item)

alive_enemies = []
dead_enemies = []

for i in range(10):
    alive_enemies.append(Enemy(items))

# Enemy setter
def room_character_setter(character):
    random.shuffle(rooms)
    for x in rooms:        
        if x.character == None:
            x.set_character(character)
            break
        else:
            x = None
 
for enemy in alive_enemies:
    room_character_setter(enemy)

current_Room = kitchen

def game(current_Room):
    while alive_enemies:
        print("\n")
        inhabitant = current_Room.get_character()
        current_Room.get_details()
        
        current_Room.room_draw()
        command = input("> ")
        command = command.lower()
        if command in ["north", "south", "east", "west"]:
            current_Room = current_Room.move(command)
        elif command == "talk":
            if inhabitant is not None:
                inhabitant.talk()
            else:
                print("\n You're talking to yourself")

        elif command == "fight":
            player_item = player_char.get_item()
            # print("You are currently holding: " + player_char.get_item_name())
            if inhabitant is not None:  # checks someone is in the room
                print("\n What will you fight with?")
                fight_with = input()  # choose what to fight with
                fight_with = fight_with.lower()
                if fight_with == "leave":
                    print("\nYou fled from the fight")
                    print("\n Press 'Enter' key to continue")
                    input()

                    continue

                if player_item is not None:
                    p_item = player_char.get_item_name()
                    if p_item.lower() == fight_with:  # checks if they are holding what they want to fight with
                        if inhabitant.fight(fight_with) == True:
                            alive_enemies.pop()
                            dead_enemies.append(alive_enemies)
                            current_Room.set_character(None)
                            if not alive_enemies:
                                print("\nYOU WIN! You killed all of the enemies in the house.")
                                print("Thanks for playing :)")
                                input()
                                break

                        # reduce the player health by -1 if they lose
                        else:
                            player_char.set_health(-1)
                            if player_char.get_health() == 1:
                                print(f"\nYou have {player_char.get_health()} life left")
                            else:
                                print(f"\nYou have {player_char.get_health()} lives left")
                            if player_char.get_health() < 1:
                                print("GAME OVER")
                                input()
                                break

                    else:
                        print("You are not holding that")
                else:
                    print("Your hands are empty")
            else:
                print("\n There are no enemies in the room to fight")


        elif command == "take":
            room_item = current_Room.get_item()
            player_item = player_char.get_item()
            if room_item is None:
                print("The room is empty")
            else:
                if player_item is None:
                    if room_item is not None:
                        player_char.set_item(room_item)
                        current_Room.set_item(None)
                        print("You are now holding the", player_char.get_item_name())
                else:
                    print("Your hands are full")

        elif command == "drop":
            room_item = current_Room.get_item()
            player_item = player_char.get_item()

            if player_item is None:
                print("Your hands are sooper dooper empty")
            else:

                if room_item is None:
                    if player_item is not None:
                        print("You dropped the", player_char.get_item_name())
                        player_char.set_item(None)
                        current_Room.set_item(player_item)
                else:
                    print("The room is full")

        elif command == "swap":
            room_item = current_Room.get_item()
            player_item = player_char.get_item()

            if player_item is None and room_item is None:
                print("You can't swap nothing for nothing")

            elif player_item is not None and room_item is None:
                print("You can't swap an item for nothing")

            elif player_item is None and room_item is not None:
                print("You can't swap nothing for an item")

            else:
                print("You swapped the " + str(current_Room.get_item_name()) + " for the " + str(
                    player_char.get_item_name()))

                if room_item is not None and player_item is not None:
                    tmp = room_item
                    current_Room.set_item(player_item)
                    player_char.set_item(tmp)
                else:
                    print("You can't swap an item for nothing")

        elif command == "item":
            player_item = player_char.get_item()
            if player_item is not None:
                print("You are currently holding: " + player_char.get_item_name())
                print(player_char.get_item_description())
            else:
                print("Your hands are empty")

        elif command == "health":
            if player_char.get_health() == 1:
                print(f"You have {player_char.get_health()} life left")
            else:
                print(f"You have {player_char.get_health()} lives left")

        elif command == "help":
            # all commands and what they do
            print("\nHere's a list of the commands you can use:")
            print(
                "\nnorth - move to the room above \neast - move to the room to the right \nsouth - move to the room below \nwest - move to the room to the left")
            print("take - pick up the item in the room you are in (you can only hold one item at a time) \ndrop - drop the item in your hands into the room (you can't drop an item if there is already an item in the room)")
            print("swap - swap the item in your hands for the item in the room")
            print("talk - talk to the enemy in the room with you \nfight - battle the enemy in the room with you \nleave - leave the fight and return when you are ready (use this command when it asks you what you will fight with)")
            print("item - view the current item in your hands")
            print("health - see how many lives you have left")
            print("quit - quit the game")

        elif command == "quit":
            break

        else:
            print("INVALID COMMAND, type 'help' to view a list of commands you can use")

        print()
        print("Press 'Enter' key to continue")
        input()


game(current_Room)