import time
import random

statList = ["Strength", "strength", "STRENGTH",
            "Dexterity", "dexterity", "DEXTERITY",
            "Constitution", "constitution", "CONSTITUTION",
            "Wisdom", "wisdom", "WISDOM",
            "Intelliegence", "intelligence", "INTELLIGENCE",
            "Charisma", "charisma", "CHARISMA", "str", 'STR',
            'Str', 'dex' 'Dex', 'DEX', 'con', 'Con', 'CON',
            'wis', 'Wis', 'WIS', 'int', 'Int', 'INT', 'cha',
            'Cha', 'CHA']


def nameSelection():
    """Lets player select name"""
    while True:
        print("Enter Your Name!")
        name = input()
        print()
        time.sleep(0.5)
        print("Are you sure, " + name + "?")
        print("Enter 'Y' to confirm, anything else to input a different name")
        print()
        nameConfirmation = input()
        if nameConfirmation in ["Y", "y", "YES", "yes", "Yes"]:
            return name
            break

def printStats():
    """Prints adjusted stat total"""
    time.sleep(0.5)
    print()
    print("Your strength (str) stat is:       ", self.strength)
    print("Your dexterity (dex) stat is:      ", self.dexterity)
    print("Your constitution (con) stat is:   ", self.constitution)
    print("Your wisdom (wis) stat is:         ", self.wisdom)
    print("Your intelligence (int) stat is:   ", self.intelligence)
    print("Your charisma (cha) stat is:       ", self.charisma)
    print()

def statChange(stat, amount):
    '''Adds stat changes'''
    if stat in ["Strength", "strength", "STRENGTH", "str", 'STR','Str']:
        self.strength += amount
    elif stat in ["Dexterity", "dexterity", "DEXTERITY", 'dex' 'Dex','DEX']:
        self.dexterity += amount
    elif stat in ["Constitution", "constitution", "CONSTITUTION", 'con', 'Con', 'CON']:
        self.constitution += amount
    elif stat in ["Wisdom", "wisdom", "WISDOM", 'wis', 'Wis', 'WIS']:
        self.wisdom += amount
    elif stat in ["Intelliegence", "intelligence", "INTELLIGENCE", 'int', 'Int', 'INT']:
        self.intelligence += amount
    elif stat in ["Charisma", "charisma", "CHARISMA", 'cha', 'Cha', 'CHA']:
        self.charisma += amount

def statSelection():
    """Let's player choose stat totals"""
    maxPoints = 24
    usablePoints = 24
    print("To add, just type a number.")
    print("Ex: 5")
    print("To subtract, type a negative number.")
    print("Ex: -5")
    print()
    while True:
        time.sleep(0.5)
        print()
        printStats()
        print()
        time.sleep(0.5)
        if usablePoints == 0:
            print("Are you okay with your stats?")
            confirmation = input()
            if confirmation in ["Y", "y", "YES", "yes", "Yes"]:
                break
        else:
            print("You have ", usablePoints," usable points")
        print()
        print("Which stat do you want to change?")
        stat = input()
        if stat not in statList:
           print("Choose an actual stat, asshole.")
           continue
        print("How much do you want to change it?")
        amount = input()
        if(amount.isdigit):
            amount = int(amount)
        else:
            print("Enter a number, dumbass.")
            continue
        if(usablePoints - amount < 0):
            print("Don't try to use points you don't have.")
            continue
        elif(usablePoints - amount > maxPoints):
            print("Don't try to get back points you don't have.")
            continue
        statChange(stat, amount)
        usablePoints -= amount            

class player():
    """Creates the player object
Gives the object D&D-like stats
and sets the name
    """
    def __init__(self):
        """Creating player statistics"""
        print()
        print("*********************")
        print("*Character Creation!*")
        print("*********************")
        time.sleep(0.5)
        print()
        print("Randomly Rolled: All stats will be given random values between 1 and 7")
        print("Pros: Potentially High Stats")
        print("Cons: Potentially Low Stats")
        print()
        time.sleep(0.5)
        print("Set point: You're given 21 points to divide between all Stats")
        print("Pros: Fair point values")
        print("Cons: No especially high stats without downsides.")
        print()
        time.sleep(0.5)
        while True:
            print("Choose One: 'Randomly' or 'Set' ")
            pointStyle = input()
            print()
            if pointStyle in ["Randomly", "randomly", "RANDOMLY"]:
                self.name = nameSelection()
                print()
                time.sleep(0.5)
                self.strength = random.randint(1, 7)
                self.dexterity = random.randint(1, 7)
                self.constitution = random.randint(1, 7)
                self.intelligence = random.randint(1, 7)
                self.wisdom = random.randint(1, 7)
                self.charisma = random.randint(1, 7)
                self.bag = {}
                self.level = 1
                self.exp = 0
                print("Hello, " + self.name + "!")
                printStats()
                break
            elif pointStyle in ["Set", "set", "SET"]:
                self.strength = 0
                self.dexterity = 0
                self.constitution = 0
                self.intelligence = 0
                self.wisdom = 0
                self.charisma = 0
                self.bag = {}
                self.level = 1
                self.exp = 0
                self.name = nameSelection()
                statSelection()
                break
            else:
                print("Enter a Correct Value, Asshole")
                print()
                time.sleep(0.5)

class inventory(object):
    pass