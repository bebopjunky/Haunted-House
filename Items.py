import random
from data import i_name,i_desc,colour,size


class Item():

    def __init__(self):
        self.name = None
        self.description = None
        self.colour = None
        self.size = None
        self.gen_rnd_item()

#setter
    def set_description(self, Item_description):
        self.description = Item_description
#getter
    def get_description(self):
        return self.description
#setter
    def set_name(self, Item_name):
        self.name = Item_name
#getter
    def get_name(self):
        return self.name
#setter
    def set_colour(self, Item_colour):
        self.colour = Item_colour
#getter
    def get_colour(self):
        return self.colour

    def gen_rnd_item(self):
        item_name = random.choice(i_name)
        item_desc = random.choice(i_desc)
        item_colour = random.choice(colour)
        item_size = random.choice(size)
        
        i_name.remove(item_name)
        i_desc.remove(item_desc)
        
        self.name = item_name
        self.description = item_desc
        self.colour = item_colour
        self.size = item_size

        #items.append(self)


