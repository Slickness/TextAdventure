import json #to get the required file

#'''This class will hold all player class and load player from json'''
def get_player():
    
    with open ("player.json","r") as f:
        jsontext = f.read()
        d = json.loads(jsontext)
       # print (d)
        player = (d["player"])
    #    print (player)
    return (Player(**player[0]))

class Player ():
    def __init__ (self,name ="default",hp = 100,maxhp = 100,armour = None,
            weapon = None, items = {}):
        self.name = name
        self.hp = hp
        self.maxhp = maxhp
        self.armour = armour
        self.weapon = weapon
        self.items = items
    def isDead(self):
        if self.hp <= 0:
            return True
        else:
            return False

