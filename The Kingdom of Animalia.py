import Entities as Ent
import time
import os

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
    print("Type 'info' to check how to play!")
    print()
    print("Please enter one:")
    print()
    viewScreen = input()
    if viewScreen.lower() == "start":
        os.system('clear')
        break
    elif viewScreen.lower() == "leaderboard":
        os.system('clear')
        print()
        print()
        pass
    elif viewScreen.lower() == "info":
        os.system('clear')
        pass
    else:
        print("Bitch, this is the fucking title screen. How the fuck you fuckin up already.")
        time.sleep(5)
        os.system('clear')
        pass

"""   Start Screen    """
p1 = Ent.player.player()
os.system('clear')


class world(object):
    '''"World" Class for subclass worlds
    Sets Level Gate, Boss Levels, '''

    def __init__(self, lG, bL):
        self.levelGate = lG
        self.bossLevel = bL


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


currentWorld = Midgard()
while True:
    print("You have moved to " + currentWorld.worldName)

    while currentWorld.worldName == "Midgard":
        pass

    while currentWorld.worldName == "Eden":
        pass

    while currentWorld.worldName == "Agartha":
        pass
