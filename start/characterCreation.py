
import time
import random

class characterCreation():
    def __init__(self):
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
                        self.name = name
                        break
                    else:
                        pass
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
                # Name Creation
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
                        self.name = name
                        break
                    else:
                        pass
                # Point Selecting
                while True:
                    print()
                    print()
                    time.sleep(1)
                    print()
                    print("Your strength stat is: ", self.strength)
                    print("Your dexterity stat is: ", self.dexterity)
                    print("Your constitution stat is: ", self.constitution)
                    print("Your wisdom stat is: ", self.wisdom)
                    print("Your intelligence stat is: ", self.intelligence)
                    print("Your charisma stat is: ", self.charisma)
                    print()
                    if ptSelection is False:
                        print("Hello, " + self.name + "!")
                        ptSelection is True
                        break
                    else:
                        pass
                    print()
                    print()
                    print()
                    time.sleep(1)
                    startPts = 0
                    statChange = input("Which stat do you want to change? ")
                    print()
                    while True:
                        if statChange in ["Strength", "STRENGTH", "strength"]:
                            print()
                        elif statChange in ["Dexterity", "DEXTERITY", "dexterity"]:
                            print()
                        elif statChange in ["Constitution", "CONSTITUTION", "consitution"]:
                            print()
                        elif statChange in ["Wisdom", "WISDOM", "wisdom"]:
                            print()
                        elif statChange in ["Intelligence", "INTELLIGENCE", "intelligence"]:
                            print()
                        elif statChange in ["Charisma", "CHARISMA", "charisma"]:
                            print()
                        else:
                            print()
                pass
                break
########################################################################################
############     Invalid Inputs     ####################################################
########################################################################################
            else:
                print("Enter a Correct Value Asshole")
                print()
                time.sleep(1)
                pass
