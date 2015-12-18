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
            weapon = None, items = {}, room = None, prevRoom = None,
            level = 1, points = 0):
        self.pointsPerLevel = 1000 #points to increase per level
        self.increasemaxhp = 10 #amount to increase max hp by
        self.name = name
        self.hp = hp
        self.maxhp = maxhp
        self.armour = armour
        self.weapon = weapon
        self.items = items
        self.room = room
        self.prevRoom = prevRoom
        self.level = level
        self.points = points
    def isDead(self):
        #determine if the player is dead
        if self.hp <= 0:
            return True
        else:
            return False
    def SetRoom(self,roomID):
        # set the new room by ID and set previous rooom
        self.prevRoom = self.room
        self.room = roomID
    def updateHP(self,damage):
        #update the players HP
        #if health increases use a neg number
        self.hp = self.hp - damage
    def updateMaxHP(self,newMax):
        #new max is new max number not how much to increase by
        self.maxhp = newMax
    def getHP(self):
        #returns the health of the player 
        return self.hp
    def getMaxHP(self):
        #returns the maxium health of the player
        return self.maxhp
    def levelUp(self):
        #increases the level of the player and increase max health
        self.level += 1
        self.updateMaxHP(self.getMaxHP+self.increasemaxhp)
        self.hp = self.getMaxHP # give player max health if they level up
 
