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

    transferText = "Put cool world travel text here"


class Midgard(world):
    '''Starting World
Contains basic enemies and first part of the story arc'''

    def __init__(self):
        super().__init__(1, 5)
        self.worldName = "Midgard"

    transferText = "Put cool world travel text here"


class Agartha(world):
    '''Underground world based off of the "Hollow Earth"
theory'''

    def __init__(self):
        super().__init__(6, 12)
        self.worldName = "Agartha"

    transferText = "Put cool world travel text here"
