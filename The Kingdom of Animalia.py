import Entities as Ent
import start

"""   Start Screen    """
begin = start.startScreen.startScreen()
p1 = Ent.player.player()

class world(): 
    '''"World" Class for subclass worlds
    Sets Level Gate, Boss Levels, '''
    def __init__(self, lG, bL):
        self.levelGate = lG
        self.bossLevel = bL

class Eden(world):
    '''Safety world.'''
    def __init__(self, lG, bL):
        super().__init__(0, 0)
        self.worldName = "Eden"
    
class Midgard(world):
    '''Starting World
Contains basic enemies and first part of the story arc'''
    def __init__(self, lG, bL):
        super().__init__(1, 5)
        self.worldName = "Midgard"

class Agartha(world):
    '''Underground world based off of the "Hollow Earth"
theory'''
    def __init__(self):
        super().__init__(6, 12)
        self.worldName = "Agartha"

currentWorld = Midgard()

if currentWorld.worldName == "Midgard":
    print("You are located in: " + currentWorld.worldName)
    