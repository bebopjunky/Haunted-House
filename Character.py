from data import m_name,m_desc
import random

class Character():

    # Create a character
    def __init__(self):
        self.name = None
        self.description = None
        self.conversation = None

    # Describe this character
    # def describe(self):
    #     print(self.name + " is here!")
    #     #print(self.description)


    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("\n [" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character):
    def __init__(self,items):
            super().__init__()
            self.weakness = None
            self.gen_rnd_monster(items)

    def set_weakness(self, enemy_weakness):     #setter
        self.weakness = enemy_weakness

    def get_weakness(self):      #getter
        return self.weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You destroyed " + self.name + " with the " + combat_item + "!" )
            return True
        else:
            print("The " + combat_item + " was ineffective against " + self.name + ", he absolutely wrecked you!")
            print("i am weak to " + self.weakness.description)
            return False
    
    def gen_rnd_monster(self,items):
        monster_name = random.choice(m_name)
        monster_desc = random.choice(m_desc)
                
        m_name.remove(monster_name)
        m_desc.remove(monster_desc)
        
        self.name = monster_name
        self.description = monster_desc
        self.weakness = random.choice(items)

        
        



class Player():
    def __init__(self, player_name):
        self.name = player_name
        self.appearance = None
        self.item = None
        self.health = 5

    def set_health (self,modifier):
        self.health = self.health + modifier

    def get_health (self):
        return self.health

    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item

    def get_item_name(self):
        return self.item.name
    
    def get_item_description(self):
        return self.item.description

    def set_appearance(self,appearance):
        self.appearance = appearance

    def get_appearance(self):
        return self.appearance