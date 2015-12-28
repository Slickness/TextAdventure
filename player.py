import json #to get the required file

#'''This class will hold all player class and load player from json'''
def get_player():
    
    with open ("game.json","r") as f:
        jsontext = f.read()
        d = json.loads(jsontext)
       # print (d)
        player = (d["player"])
    #    print (player)

    return (Player(**player[0]))

class Player ():
    def __init__ (self,name ="default",hp = 100,maxhp = 100,
            armour = 0,
            weapon = 2, items = {}, room = None, prevRoom = None,
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
        return self.hp <=0
    def SetRoom(self,roomID):
        # set the new room by ID and set previous rooom
        #not working - fixed was calling the function twice
        old = self.room
        self.prevRoom = old
        self.room = roomID
    def updateHP(self,damage):
        #update the players HP
        #if health increases use a neg num ber
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
        print ("in level up")
        self.level = int(self.level) + 1
        self.updateMaxHP(int(self.getMaxHP())+int(self.increasemaxhp))
         # give player max health if they level up
        self.hp = int(self.getMaxHP())
    def updatePoints(self,newPoints):
        #update the points fo the player and determine if they level up
        self.points += int(newPoints)
        increase = 1
        while increase == 1:
            pointsForLevel = self.pointsPerLevel*self.level
            if int(self.points) >= int(pointsForLevel):
                self.levelUp()
            else:
                increase = 0
    def addItem(self,newItem):
        #used to input item into dictionary
        self.items[newItem] = True
    def _item(self,item):
        #check to see if the key is in the list and if it usuable
        return self.items.get(item,False) #get the value or False
