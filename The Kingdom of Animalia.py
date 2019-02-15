import Entities as Ent
import start

"""   Start Screen    """
begin = start.startScreen.startScreen()
if begin.createPlayer is True:
    """  Character Creation  """
    p1 = Ent.player.player()
