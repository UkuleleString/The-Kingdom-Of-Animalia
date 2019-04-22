import Entities as Ent
import time
import os
import pickle

while True:
    print("********************")
    print("*    Welcome to    *")
    print("*     The Game     *")
    print("*        <3        *")
    print("********************")
    print()
    print("Type 'Start' to start the game")
    print()
    print("Type 'Leaderboard' to look at your top scores!")
    print()
    print("Type 'Load' to load a save game!")
    print()
    print("Please enter one:")
    print()
    viewScreen = input()
    if viewScreen.lower() == "start":
        p1 = Ent.player.player()
        os.system('clear')
        break
    elif viewScreen.lower() == "leaderboard":
        os.system('clear')
        print()
        print()
        pass
    elif viewScreen.lower() == "load":
        os.system('clear')
        with open('playerData.pkl', 'rb') as playerData:
            p1 = pickle.load(playerData)
        with open('worldData.pkl', 'rb') as worldData:
            currentWorld = pickle.load(worldData)
            print("Welcome back, " + p1.name + "!")
            p1.printStats()
            time.sleep(5)
        break
    else:
        print(
            "Bitch, this is the fucking title screen. How the fuck you fuckin up already.")
        time.sleep(5)
        os.system('clear')
        pass

"""   Starting the Game   """
os.system('clear')


class world(object):
    '''"World" Class for subclass worlds
    Sets Level Gate, Boss Levels, '''

    def __init__(self, levelGate, bossLevel):
        self.levelGate = levelGate
        self.bossLevel = bossLevel


class Eden(world):
    '''Safety world.'''

    def __init__(self):
        super().__init__(0, 0)
        self.worldName = "Eden"


class Midgard(world):
    '''Starting World
Contains basic enemies and first part of the story arc'''

    def __init__(self):
        super().__init__(1, 5)
        self.worldName = "Midgard"


class Agartha(world):
    '''Underground world based off of the "Hollow Earth"
theory'''

    def __init__(self):
        super().__init__(6, 12)
        self.worldName = "Agartha"

# Starts player in Midgard
# Sets all quests to uncompleted
if viewScreen.lower() == 'start':
    currentWorld = Midgard()
    questCompletion = [0]

while True:
    print("You have moved to " + currentWorld.worldName)

    while currentWorld.worldName == "Midgard":
        print("What would you like to do?")
        playerAction = input()
        if playerAction.lower() == "help":
            os.system('clear')
            print("Put info here")
            print()
            print("*******************************************************")
            print()
            print("Go to the 'Tavern' to pick up rumors or talk to patrons")
            print("Go to the 'Dungeon' to level up or find items")
            print("Go to the 'Shop' to use your gold to buy equipment")
            print("Use the 'Portal' to go to other worlds")
            print("Use 'save' to save the game")
        elif playerAction.lower() == "Tavern":
            os.system('clear')
            pass
        elif playerAction.lower() == "Dungeon":
            os.system('clear')
            pass
        elif playerAction.lower() == "Shop":
            os.system('clear')
            pass
        elif playerAction.lower() == "Portal":
            os.system('clear')
            print('')
            print("Where would you like to go?")
            transferWorld = input()
            if transferWorld.lower() == 'eden' & p1.level >= Eden.levelGate:
                print('')
                pass
        elif playerAction.lower() == "save":
            os.system('clear')
            with open('playerData.pkl', 'wb') as playerData:
                pickle.dump(p1, playerData)
            with open('worldData.pkl', 'wb') as worldData:
                pickle.dump(currentWorld, worldData)
                print('Game Saved!')

    while currentWorld.worldName == "Eden":
        pass

    while currentWorld.worldName == "Agartha":
        pass
