import random


class Die:
    def __init__(self, sides: int):
        self.current = None
        self.modified_current = None
        self.rolled = []
        self.modified_rolls = []
        self.sides = sides

    def roll(self):
        result = random.randrange(1, self.sides + 1)
        self.rolled.append(result)
        self.current_roll()

    def current_roll(self):
        if len(self.rolled) > 0:
            self.current = self.rolled[-1]
            self.modified_current = self.current  # modified current is what is currently read by display_rolls

    def modify_roll(self, operator, number):
        result = operator(self.current, number)
        self.modified_current = result
        self.modified_rolls.append(result)


class Dice:
    def __init__(self, count, sides, operator, mod):
        self.dice_list = []
        self.count = count
        self.sides = sides
        self.operator = operator
        self.mod = mod

    def rolls(self):
        self.dice_list = [Die(self.sides) for _ in range(self.count)]

        for die in self.dice_list:
            die.roll()
            if self.operator:
                die.modify_roll(self.operator, self.mod)

    def display_rolls(self):
        print("rolled:")
        for die in self.dice_list:
            print(die.modified_current)
