import random
import textwrap
import time

import Entities as Ent
import start

#####   Start Screen    #####
begin = start.startScreen.startScreen()
if begin.createPlayer == True:
    #####   Character Creation  #####
    p1 = Ent.player.player()
