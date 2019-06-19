import time
import random
import os

statList = ["Strength", "strength", "STRENGTH",
            "Dexterity", "dexterity", "DEXTERITY",
            "Constitution", "constitution", "CONSTITUTION",
            "Wisdom", "wisdom", "WISDOM",
            "Intelliegence", "intelligence", "INTELLIGENCE",
            "Charisma", "charisma", "CHARISMA", "str", 'STR',
            'Str', 'dex', 'Dex', 'DEX', 'con', 'Con', 'CON',
            'wis', 'Wis', 'WIS', 'int', 'Int', 'INT', 'cha',
            'Cha', 'CHA']


def nameSelection():
    """Lets player select name"""
    while True:
        print("Enter Your Name!")
        name = input()
        time.sleep(0.5)
        print("\nAre you sure, " + name + "?")
        print("Enter 'Y' to confirm, anything else to input a different name\n")
        nameConfirmation = input()
        if nameConfirmation in ["Y", "y", "YES", "yes", "Yes"]:
            return name
            break


class player():
    """Creates the player object
Gives the object D&D-like stats
and sets the name
    """

    def printStats(self):
        """Prints adjusted stat total"""
        print("**************************************************")
        print("Your strength (str) stat is:       ", self.strength)
        print("Your dexterity (dex) stat is:      ", self.dexterity)
        print("Your constitution (con) stat is:   ", self.constitution)
        print("Your wisdom (wis) stat is:         ", self.wisdom)
        print("Your intelligence (int) stat is:   ", self.intelligence)
        print("Your charisma (cha) stat is:       ", self.charisma)
        print("**************************************************\n")

    def statChange(self, stat, amount):
        '''Adds stat changes'''
        if stat in ["Strength", "strength", "STRENGTH", "str", 'STR', 'Str']:
            self.strength += amount
        elif stat in ["Dexterity", "dexterity", "DEXTERITY", 'dex', 'Dex', 'DEX']:
            self.dexterity += amount
        elif stat in ["Constitution", "constitution", "CONSTITUTION", 'con', 'Con', 'CON']:
            self.constitution += amount
        elif stat in ["Wisdom", "wisdom", "WISDOM", 'wis', 'Wis', 'WIS']:
            self.wisdom += amount
        elif stat in ["Intelliegence", "intelligence", "INTELLIGENCE", 'int', 'Int', 'INT']:
            self.intelligence += amount
        elif stat in ["Charisma", "charisma", "CHARISMA", 'cha', 'Cha', 'CHA']:
            self.charisma += amount

    def statSelection(self):
        """Let's player choose stat totals"""
        maxPoints = 21
        usablePoints = 21
        usedPoints = 0
        print("To add, just type a number.")
        print("Ex: 5")
        print("To subtract, type a negative number.")
        print("Ex: -5\n")
        while True:
            self.printStats()
            if usablePoints == 0:
                print("Are you okay with your stats?")
                confirmation = input()
                if confirmation in ["Y", "y", "YES", "yes", "Yes"]:
                    break
            else:
                print("You have ", usablePoints, " usable points")
                print("You have used ", usedPoints, " points\n")
            print("Which stat do you want to change?")
            stat = input()
            if stat not in statList:
                print("\nChoose an actual stat, asshole.")
                time.sleep(1)
                os.system('clear')
                continue
            print("\nHow much do you want to change it?")
            amountStr = input()
            amount = ''
            negativeNum = False
            for character in amountStr:
                if character == "-":
                    negativeNum = True
                elif character.isdigit:
                    amount = str(amount) + character
                else:
                    os.system('clear')
                    print("\nEnter a number, dumbass.")
                    continue
            amount = int(amount)
            if negativeNum is True:
                amount = 0 - amount
            usablePoints -= amount
            usedPoints += amount
            if(usablePoints < 0):
                os.system('clear')
                print("\nDon't try to use points you don't have.")
                usablePoints += amount
                usedPoints -= amount
                continue
            elif(usedPoints > maxPoints):
                os.system('clear')
                print("\nDon't try to get back points you don't have.")
                usablePoints += amount
                usedPoints -= amount
                continue
            self.statChange(stat, amount)
            os.system('clear')

    def __init__(self):
        """Creating player statistics"""
        print("*********************")
        print("*Character Creation!*")
        print("*********************\n")
        time.sleep(0.5)
        print("Randomly Rolled: All stats will be given random values between 1 and 7")
        print("Pros: Potentially High Stats")
        print("Cons: Potentially Low Stats\n")
        time.sleep(0.5)
        print("Set point: You're given 21 points to divide between all Stats")
        print("Pros: Fair point values")
        print("Cons: No especially high stats without downsides.\n")
        time.sleep(0.5)
        while True:
            print("Choose One: 'Randomly' or 'Set'\n")
            pointStyle = input()
            if pointStyle.lower() in ["randomly", "random", "rand"]:
                os.system('clear')
                self.name = nameSelection()
                time.sleep(0.5)
                os.system('clear')
                self.strength = random.randint(1, 7)
                self.dexterity = random.randint(1, 7)
                self.constitution = random.randint(1, 7)
                self.intelligence = random.randint(1, 7)
                self.wisdom = random.randint(1, 7)
                self.charisma = random.randint(1, 7)
                self.statusEffects = []
                self.bag = {}
                self.level = 1
                self.exp = 0
                print("Hello, " + self.name + "!")
                self.printStats()
                time.sleep(5)
                break
            elif pointStyle.lower() == "set":
                os.system('clear')
                self.strength = 0
                self.dexterity = 0
                self.constitution = 0
                self.intelligence = 0
                self.wisdom = 0
                self.charisma = 0
                self.statusEffects = []
                self.bag = {}
                self.level = 1
                self.exp = 0
                self.name = nameSelection()
                os.system('clear')
                self.statSelection()
                time.sleep(1)
                break
            else:
                print("Enter a Correct Value, Asshole")
                time.sleep(5)
                os.system('clear')

if __name__ == "__main__":
    p1 = player()
