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
        self.operator = operator  # will be None if no operator is entered as part of input
        self.mod = mod
        self.sum = None
        self.sum_individual_modified = None
        self.sum_modified = None

    def rolls(self):
        self.dice_list = [Die(self.sides) for _ in range(self.count)]

        for die in self.dice_list:
            die.roll()
            if self.operator:
                die.modify_roll(self.operator, self.mod)

        self.sum_individual_modified = sum(die.modified_current for die in self.dice_list)

        self.sum = sum(die.current for die in self.dice_list)

        if self.operator:
            self.sum_modified = self.operator(self.sum, self.mod)

    def modify_rolls(self):
        total = sum(die.current for die in self.dice_list)
        self.sum_modified = self.operator(total, self.mod)

    def display_rolls(self):
        print("rolled:")
        for die in self.dice_list:
            print(die.modified_current)
            print(f"total: {self.sum_individual_modified}")
            
    def display_verbose(self):
        count = 0
        if self.operator:
            print(f"Rolled {self.count}d{self.sides} with a modifier of {self.operator}{self.mod}")
            for die in self.dice_list:
                print(f"Die {count}: {die.current}")
                count += 1
            print(f"The total is {self.sum} modified to {self.sum_modified}")
        else:
            print(f"Rolled {self.count}d{self.sides}")
            for die in self.dice_list:
                print(f"Die {count}: {die.current}")
                count += 1
            print(f"The total is: {self.sum}")

