import time
import random

############################################################
############         Creation Class         ################
############################################################


class characterCreation():
    def __init__(self):
        """Creating player statistics"""
    ############################################
    ####   Commands just to clean up code   ####
    ############################################
        def nameSelection():
            """Lets player select name"""
            while True:
                print("Enter Your Name!")
                name = input()
                print()
                time.sleep(1)
                print("Are you sure, " + name + "?")
                print("Enter 'Y' to confirm, anything else to input a different name")
                print()
                nameConfirmation = input()
                if nameConfirmation in ["Y", "y", "YES", "yes", "Yes"]:
                    return name
                    break

        def printStats():
            """Prints adjusted stat total"""
            time.sleep(1)
            print()
            print()
            print("Your strength stat is: ", self.strength)
            print("Your dexterity stat is: ", self.dexterity)
            print("Your constitution stat is: ", self.constitution)
            print("Your wisdom stat is: ", self.wisdom)
            print("Your intelligence stat is: ", self.intelligence)
            print("Your charisma stat is: ", self.charisma)
            print()

        def statChange(stat, amount):
            if stat in ["Strength", "strength", "STRENGTH"]:
                self.strength += amount
            elif stat in ["Dexterity", "dexterity", "DEXTERITY"]:
                self.dexterity += amount
            elif stat in ["Constitution", "constitution", "CONSTITUTION"]:
                self.constitution += amount
            elif stat in ["Wisdom", "wisdom", "WISDOM"]:
                self.wisdom += amount
            elif stat in ["Intelliegence", "intelligence", "INTELLIGENCE"]:
                self.intelligence += amount
            elif stat in ["Charisma", "charisma", "CHARISMA"]:
                self.charisma += amount

        def statSelection():
            """Let's player choose stat totals"""
            startGame = True
            startPts = 0
            maxPoints = 21
            while True:
                if startGame is True:
                    print("To add, just type a number.")
                    print("Ex: 5")
                    print("To subtract, type a negative number")
                    print("Ex: -5")
                    startGame = False
                    print()
                    print()
                stat = input("Which stat do you want to change? ")
                print()
                print()
                printStats()
                print()
                print()
                time.sleep(1)



    #####################################
    ####        Actual  class        ####
    #####################################

        print()
        print("*********************")
        print("*Character Creation!*")
        print("*********************")
        time.sleep(1)
        print()
        print("Randomly Rolled: All stats will be given random values between 1 and 7")
        print("Pros: Potentially High Stats")
        print("Cons: Potentially Low Stats")
        print()
        time.sleep(1)
        print("Set point: You're given 21 points to divide between all Stats")
        print("Pros: Fair point values")
        print("Cons: No especially high stats without downsides.")
        print()
        time.sleep(1)
        while True:
            print("Choose One: 'Randomly' or 'Set' ")
            pointStyle = input()
            print()
########################################################################################
############               Random Point Value Choice              ######################
########################################################################################
            if pointStyle in ["Randomly", "randomly", "RANDOMLY"]:
                self.name = nameSelection()
                print()
                time.sleep(1)
                self.strength = random.randint(1, 7)
                self.dexterity = random.randint(1, 7)
                self.constitution = random.randint(1, 7)
                self.intelligence = random.randint(1, 7)
                self.wisdom = random.randint(1, 7)
                self.charisma = random.randint(1, 7)
                self.bag = {}
                print("Hello, " + self.name + "!")
                print("Your strength stat is: ", self.strength)
                print("Your dexterity stat is: ", self.dexterity)
                print("Your constitution stat is: ", self.constitution)
                print("Your wisdom stat is: ", self.wisdom)
                print("Your intelligence stat is: ", self.intelligence)
                print("Your charisma stat is: ", self.charisma)
                break
########################################################################################
############     Point Value Selection Choice        ###################################
########################################################################################
            elif pointStyle in ["Set", "set", "SET"]:
                self.strength = 0
                self.dexterity = 0
                self.constitution = 0
                self.intelligence = 0
                self.wisdom = 0
                self.charisma = 0
                self.bag = {}
                self.name = nameSelection()
                statSelection()
                break
########################################################################################
############     Invalid Inputs     ####################################################
########################################################################################
            else:
                print("Enter a Correct Value Asshole")
                print()
                time.sleep(1)
