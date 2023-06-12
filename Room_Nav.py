import random
from data import r_name
#attributes
class Room():
    def __init__(self):
        self.name = None
        self.description = None
        self.linked_Rooms = {}
        self.character = None
        self.item = None
        self.rnd_room_gen()

    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item

    def get_item_name(self):
        return self.item.name

#setter
    def set_description(self, Room_description):
        self.description = Room_description
#getter
    def get_description(self):
        return self.description
#setter
    def set_name(self, Room_name):
        self.name = Room_name
#getter
    def get_name(self):
        return self.name

#setter for character in room
    def set_character(self, character):
        self.character = character

#getter for character in room
    def get_character(self):
        return self.character
    
    def get_character_name(self):
        return self.item.name

    def describe(self):
        print(self.description)

    def link_Room(self,Room_to_link, direction):
        self.linked_Rooms[direction] = Room_to_link

    def get_details(self):
        
        print(self.name)
        print("---------------------------")
        print(self.description)
        for direction in self.linked_Rooms:
            Room = self.linked_Rooms[direction]
            print( "The " + Room.get_name() + " is " + direction)
        print("---------------------------")
                
        room_item = self.item
        print("ITEM:")
        if room_item is not None:
            print(self.item.name)
            print(self.item.description)
        else:
            print("There are no items in this room")
       
        inhabitant = self.get_character()
        print("")
        print("ENEMEY:")
        if inhabitant is not None:
            print(self.character.name)
            print(self.character.description)
            
        else:
            print("There are no enemies in the room")

    def move (self, direction):
        if direction in self.linked_Rooms:
            return self.linked_Rooms[direction]
        else:
            print("You can't go that way! ")
            return self

    def room_draw(self):
        n_door = False
        s_door = False
        e_door = False
        w_door = False
        r_item = False
        r_character = False

        if "north" in self.linked_Rooms:
            n_door = True
        if "south" in self.linked_Rooms:
            s_door = True
        if "east" in self.linked_Rooms:
            e_door = True
        if "west" in self.linked_Rooms:
            w_door = True
        if self.item is not None:
            r_item = True
        if self.character is not None:
            r_character = True

        if n_door == True:
            print("\n-----/ ------")
        else:
            print("\n-------------")

        print("|           |")

        if r_item == True:
            print("|     i     |")
        else:
            print("|           |")

        print("|           |")

        if e_door == True and w_door == True:
            print("/           /")
        elif e_door == True:
            print("|           /")
        elif w_door == True:
            print("/           |")
        else:
            print("|           |")
        
        if r_character == True:
            print("|     e     |")
        else:
            print("|           |")

        print("|           |")

        if s_door == True:
            print("-----/ ------\n")
        else:
            print("-------------\n")

    def rnd_room_gen(self):
        #room_name = ["dormitory","kitchen","storage","guardroom","treasure room"]
        room_floor =["covered by blood","covered by bones","covered by rugs/furs","covered by moss/mushrooms","covered by books/papers"]
        room_walls =["covered by tapestries","covered by paintings","covered by vines"]

        room_name = random.choice(r_name)
        r_name.remove(room_name)
        self.name = room_name

    def rnd_room_nav(self,new_rooms):
        links = (random.randint(0, 3))
        directions = ["north","south","east","west"]  
        
        tmp_list = []
        tmp_list.clear()
        tmp_list = new_rooms.copy()

        while links > -1:
            direction = random.choice(directions)
            if direction == "north":                
                opposite_direction = "south"
            elif direction == "south":                
                opposite_direction = "north"
            elif direction == "east":                
                opposite_direction = "west" 
            elif direction == "west":                
                opposite_direction = "east"

                           
            found = False
            while found == False:
                linking_room = tmp_list[0]                             
                if opposite_direction in linking_room.linked_Rooms:                    
                    #tmp_list.remove(linking_room)   
                    linking_room = tmp_list[0]
                else:
                    found = True
                

            self.link_Room(linking_room,direction)
            linking_room.link_Room(self,opposite_direction)
            directions.remove(direction)
            tmp_list.remove(linking_room)   
            links = links -1

   
    #def link_two_rooms(room_a,room_b):

