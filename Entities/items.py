class item(object):
    """Creates Items. Sets Identification, name, and other such things."""

    def __init__(self, iD, name):
        self.id = iD
        self.name = name


class weapon(item):
    """Creates Weapons"""

    def __init__(self, iD, name):
        pass
