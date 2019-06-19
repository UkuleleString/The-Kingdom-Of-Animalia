class timer(object):
    """Creates timer to return values based on
what period of the day it is"""

    def __init__(self):
        self.minutes = 15
        self.hours = 0

    def checktime(self):
        hour = int(self.minutes / 60)
        hour /= 18
        return hour

    def quarterPass(self):
        self.minutes += 15

    def wholePass(self):
        self.minutes += 60
