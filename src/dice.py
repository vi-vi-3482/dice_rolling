import random
import operator


class Die:
    def __init__(self, sides: int):
        self.current = None
        self.modified_current = None
        self.rolled = []
        self.modified_rolls = []
        self.sides = sides

    def roll(self):
        result = random.randrange(1, self.sides+1)
        self.rolled.append(result)
        self.current_roll()

    def current_roll(self):
        if len(self.rolled) > 0:
            self.current = self.rolled[-1]

    def modify_roll(self, operator, number):
        result = operator(self.current, number)
        self.modified_current = result
        self.modified_rolls.append(result)


class Dice:
    def __init__(self):
        pass
    def roll(self, count, sides):
        dice_list = [Die(sides) for _ in range (3)]

        return dice_list