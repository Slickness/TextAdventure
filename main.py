#!/usr/bin/python3
import sys
import colors
import cmd
import os
from room import get_blocks
from player import get_player
from enemy import get_enemy
import textwrap


class Game(cmd.Cmd):
    def Splash(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("welcome")

    def __init__(self):
        self.intro = self.Splash()
        self.prompt = "Action >>"
        cmd.Cmd.__init__(self)
        self.player = get_player()
        self.blocks = get_blocks()
        self.enemies = get_enemy()
        self.getRoom("F1")
        self.notBattle = True  # if not in battle continue as normal

    def battle(self):

        self.getEnemy(self.loc.enemy)
        enemyInfo = "You are in a battle with " +\
                    self.eBattle.name + " " +\
                    "with a \nHealth of " + str(self.eBattle.hp) + " " +\
                    "and \nAttack power of " + str(self.eBattle.attack) +\
                    "\nWould you like to run or attack?"
        self.printScreen(enemyInfo)

    def getRoom(self, room):
        for x in self.blocks:
            if x.ident == room:
                self.loc = x
        self.player.SetRoom(self.loc.ident)

    def getEnemy(self, enemy):
        for x in self.enemies:
            if x.name == enemy:
                self.eBattle = x

    def move(self, direction):
        if self.notBattle:
            newroom = self.loc._neighbour(direction)
            # check to see if newroom is in the neighbour list if not
            # tell the user it is not a valident move and do nothing
            if newroom is None:
                self.printScreen("You can not go that way")
            else:
                if newroom["keyrequired"] == "No":
                    self.getRoom(newroom["ident"])
                    self.printScreen(self.loc.name)
                else:
                    if self.player._item(newroom["key"]):
                        self.getRoom(newroom["ident"])
                        self.printScreen(self.loc.name)
                    else:
                        self.printScreen("a key is required")
                if self.loc.hasEnemy:
                    self.notBattle = False
                    self.battle()
        else:
            self.default(direction)

    def printScreen(self, text):
        # call this function each time you want to print
        os.system('cls' if os.name == 'nt' else 'clear')
        if self.player.isDead():
            os.system('cls' if os.name == 'nt' else 'clear')
            print ("you are dead")
            raise SystemExit
        else:
            if os.name == 'nt':
                print ("HEALTH ",
                       str(self.player.getHP()), "/",
                       str(self.player.getMaxHP()),
                       " WEAPON", self.player.weapon,
                       "   ARMOUR ", self.player.armour,
                       "     LEVEL ", self.player.level,
                       "     POINTS ", self.player.points,
                       "\n")
            else:
                print (colors.HEADER, colors.BACKGROUND, "HEALTH ",
                       str(self.player.getHP()), "/",
                       str(self.player.getMaxHP()),
                       "   ARMOUR ", self.player.armour,
                       " WEAPON", self.player.weapon,
                       "     LEVEL ", self.player.level,
                       "     POINTS ", self.player.points,
                       colors.ENDC, colors.ENDC, "\n")
                for line in textwrap.wrap(text,
                                          replace_whitespace=False,
                                          width=60):
                    print(line)
                print ("\n")

    def default(self, line):
        self.printScreen("command no recognized")

    def do_pickup(self, args):
        # make an update incase they enter more then one word
        item = self.loc._item(args.lower())
        if item is None:
            self.printScreen("item not there")
        elif args.lower() == "key":
            self.player.updatePoints(item[1])
            self.player.addItem(item[0])
            self.loc.removeItem(args)
            self.printScreen("you picked up a %s" % args)
        elif args.lower() == "armour":
            self.player.increaseArmour(item[0])
            self.player.updatePoints(item[1])
            self.loc.removeItem(args)
            self.printScreen("you picked up %s worth %d" % (args,item[0]))
        elif args.lower() == "weapn":
            self.player.increaseWeapon(item[0])
            self.player.updatePoints(item[1])
            self.loc.removeItem(args)
            self.printScreen("you picked up an increased %s word %d" %(args,item[0]))

    def do_look(self, args):
        text = self.loc.description
        if len(self.loc.returnItems()) > 0:
            text = text + "\nThese items look interesting:\n"
            for item in self.loc.returnItems():
                text = text + item.upper() + "\n"
        self.printScreen(text)

    def do_name(self, name):

        '''makes the ability to change your name\
        \nType name followed by your wanted name\
        \nExample name player'''
        self.player.name = name
        self.prompt = str(name) + ">>"
        self.printScreen("")

    def do_go(self, args):
        '''This is how you move type go followedby the direction
        Example: go N
        '''
        args = args.lower().strip()
        directions = ("n", "s", "e", "w")
        if args in directions:
            self.move(args)
        else:
            self.default(args)

    def do_quit(self, args):
        """leaves the game"""

        self.printScreen("Thank you for playing")
        return True

    def do_run(self, args):
        if not self.notBattle:
            self.getRoom(self.player.prevRoom)
            self.player.SetRoom(self.loc.ident)
            self.printScreen(self.loc.name)
            self.notBattle = True
        else:
            self.default(args)

    def do_attack(self, args):
        if not self.notBattle:
            # get player and enmey health
            self.eBattle.updateHp(self.player.weapon)
            # get player and enemy attack power
            # get player armour
            # calculate players damage update HP and armour health
            damage = self.eBattle.attack - ((self.player.armour / 100) *
                                            self.eBattle.attack)
            self.player.updateHP(damage)
            # check to see if player is dead
            # if not dead go back to battle
            # cheack to see if enemy is dead
            # if dead award points and change battle to false
            # and change enemy in block to false
            if self.player.isDead():
                self.printScreen("Oh Oh you have died! \n thank you \
                playing")
                sys.exit()
            elif self.eBattle.isDead():
                self.player.updatePoints(self.eBattle.points)
                self.loc.hasEnemy = False
                self.notBattle = True
                message = ("you beat " + self.eBattle.name +
                           " CONGRATS")
                self.printScreen(message)
            else:
                self.battle()
        else:
            self.default(args)

if __name__ == "__main__":
    # Try to set widentth and height of screen
    # os.popen("stty cols 80").read()
    # os.popen("stty rows 34").read()

    g = Game()
    g.cmdloop()
