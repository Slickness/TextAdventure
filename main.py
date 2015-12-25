#!/usr/bin/python3
import colors
import cmd
import os
from room import get_blocks
from player import get_player

class Game(cmd.Cmd):
    def Splash(self):
        os.system('cls' if os.name=='nt' else 'clear')
        print ("welcome")
    def __init__(self):
        self.intro = self.Splash()
        #print (blocks)
        self.prompt  = "Action >>"
        cmd.Cmd.__init__(self)
        self.player = get_player()
        self.blocks = get_blocks()
        self.getRoom("F1")
        self.notBattle = True #if not in battle continue as normal       
    def getRoom(self,room):
        for x in self.blocks:
            if x.ident == room:
                self.loc = x
        self.player.SetRoom(self.loc.ident)
    def move(self,direction):
        if self.notBattle:
            newroom = self.loc._neighbour(direction)
            #check to see if newroom is in the neighbour list if not
            #tell the user it is not a valident move and do nothing
            if newroom is None:
                self.printScreen("You can not go that way")
            else:
                if newroom["keyrequired"] == "No":
                    self.getRoom(newroom["ident"])
                    self.player.SetRoom(self.loc.ident)
                    self.printScreen(self.loc.name)
                else:
                    if self.player._item(newroom["key"]):
                        self.getRoom(newroom["ident"])
                        self.player.SetRoom(self.loc.ident)
                        self.printScreen(self.loc.name)
                    else:
                        self.printScreen("a key is required")
        else:
            self.default()
    def printScreen(self,text):
        #call this function each time you want to print
        os.system('cls' if os.name=='nt' else 'clear')
        if self.player.isDead():

            os.system('cls' if os.name=='nt' else 'clear')
            print ("you are dead")
            raise SystemExit 
            #self.do_quit("q")
        else:
            if os.name == 'nt':
                print ("HEALTH " , 
                    str(self.player.getHP()), "/",
                    str(self.player.getMaxHP()),
                    "     ", self.player.name,
                    "     LEVEL ",self.player.level,
                    "     POINTS ",self.player.points,
                    "\n")
            else:
                print (colors.HEADER,colors.BACKGROUND,"HEALTH " , 
                    str(self.player.getHP()), "/",
                    str(self.player.getMaxHP()),
                    "     ", self.player.name,
                    "     LEVEL ",self.player.level,
                    "     POINTS ",self.player.points,
                    colors.ENDC,colors.ENDC,"\n")
            print (text) 
   
    def default(self,line):
       self.printScreen("command no recognized")
    def do_pickup(self,args):
        #make an update incase they enter more then one word
        item = self.loc._item(args)
        if item == None:
            self.printScreen("item not there")
        else:
            self.player.updatePoints(item[1])
            self.player.addItem(item[0])
            self.loc.removeItem(args)
            self.printScreen("you picked up a %s"%args)
    def do_look(self,args):
        text = self.loc.description
        if len(self.loc.returnItems())>0:
            text = text + "\nThese items look interesting:\n"
            for item in self.loc.returnItems():
                text = text + item + "\n"

        self.printScreen(text)
    def do_name(self,name):

        '''makes the ability to change your name\
        \nType name followed by your wanted name\
        \nExample name player'''
        self.player.name = name
        self.prompt = str(name)+ ">>"
        self.printScreen("")   
    def do_go(self, args):
        '''This is how you move type go followedby the direction
        Example: go N
        '''
        args = args.lower().strip()

        directions = ("n","s","e","w")

        if args in directions:
            self.move(args)
        else:
            self.default(args)
    def do_quit(self, args):
        """leaves the game"""

        self.printScreen("Thank you for playing")
        return True



if __name__=="__main__":
    #Try to set widentth and height of screen 
    #os.popen("stty cols 80").read()
    #os.popen("stty rows 34").read()

    g=Game()
    g.cmdloop()
