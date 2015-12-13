#!/usr/bin/python3
import cmd
import os

class Game(cmd.Cmd):
    #def __init__(self):
    #cmd.Cmd.__init__(self)
    try:
        os.sysem('cls')
    except:
        os.system('clear')
    os.environ['LINES'] = "25"
    os.environ['COLUMNS'] = "4"
    intro = "Welcome to the Text Adventure"
    prompt  = "Action >>"
    def printScreen(self,text):
        os.system('cls' if os.name=='nt' else 'clear')
        print ("health")
        print (text)  
    def do_n(self,args):
        """Go North"""
        self.printScreen("you went north")
    def do_e(self,args):
        """Go East"""
        print ("welcome to the east direction")
    def do_w(self,args):
        """Go West"""
        pass
    def do_s(self,args):
        """Go South"""
        pass
    def do_quit(self, args):
        """leaves the game"""
        print ("Thank you for playing")
        return True



if __name__=="__main__":
    g=Game()
    g.cmdloop()
