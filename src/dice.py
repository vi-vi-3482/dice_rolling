import random


class Die:
    def __init__(self, sides: int):
        self.current = None
        self.rolled = []
        self.sides = sides

    def roll(self):
        result = random.randrange(1, self.sides+1)
        self.rolled.append(result)
        self.current_roll()

    def current_roll(self):
        if len(self.rolled) > 0:
            self.current = self.rolled[-1]

