#!/usr/bin/python3
import cmd
import os
from room import get_blocks


class Game(cmd.Cmd):
    def Splash():
        os.system('cls' if os.name=='nt' else 'clear')
        print ("welcome")
    intro = Splash()
    #print (blocks)
    prompt  = "Action >>"
    def __init__(self):
        cmd.Cmd.__init__(self)
        
        self.blocks = get_blocks()
        self.getRoom("F1")
    def getRoom(self,room):
        for x in self.blocks:
            if x.id == room:
                
                self.loc = x

    def move(self,dir):
        newroom = self.loc._neighbour(dir)
        #newroom = self.loc._neighbours(dir)
        if newroom is None:
            print("You can not go that way")
        else:
            if newroom["keyrequired"] == "No":
                self.getRoom(newroom["id"])
                print (self.loc.name)
            else:
                print ("a key is required")

            #self.loc = 

    def printScreen(self,text):
        os.system('cls' if os.name=='nt' else 'clear')
        print ("health")
        print (text) 
    def do_name(self,name):
        '''makes the ability to change your name 
Type name followed by your wanted name
Exampe name player'''
        self.prompt = str(name)+ ">>"
        self.printScreen("")   
    def do_n(self,args):
        """Go North"""
        self.move("n")
    def do_e(self,args):
        """Go East"""
        self.move("e")
    def do_w(self,args):
        """Go West"""
        self.move("w")
    def do_s(self,args):
        """Go South"""
        self.move("s")
    def do_quit(self, args):
        """leaves the game"""
        print ("Thank you for playing")
        return True



if __name__=="__main__":
    #Try to set width and height of screen 
    os.popen("stty cols 80").read()
    os.popen("stty rows 34").read()

    g=Game()
    g.cmdloop()
