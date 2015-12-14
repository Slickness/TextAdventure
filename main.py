#!/usr/bin/python3
import cmd
import os


class Game(cmd.Cmd):
    def Splash():
        os.system('cls' if os.name=='nt' else 'clear')
        print ("welcome")
    intro = Splash()
    prompt  = "Action >>"
    
    
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
    #Try to set width and height of screen 
    os.popen("stty cols 80").read()
    os.popen("stty rows 34").read()

    g=Game()
    g.cmdloop()
