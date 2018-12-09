from random import randint

class Die():
    """A class for representing a single die"""

    def __init__(self, num_sides=6):
        """a six side die"""
        self.num_sides = num_sides

    def roll(self):
        """return a random number between 1 to 6"""
        return randint(1, self.num_sides)