import operator
import re


def single_dice():
    while True:
        d = input("Dice size?")
        try:
            d = int(d)
            return d
        except ValueError:
            print("Not an integer.")


class CLI:

    def __init__(self):
        self.string_in = None

    def input_prompt(self):
        self.string_in = input("Enter dice to roll: \n")
        self.string_in.strip()
        self.string_in.lower()

    class BasicRoll:
        """
        reads dice in the form of 3d6+2
        """
        def __init__(self, dice_input):
            self.operator = None
            self.sides = None
            self.count = None
            self.mod = None
            self.pattern = re.compile(r'(\d*)d(\d+)([+\-*/])?(\d+)?')
            self.dice_input = dice_input

        def read_input(self):

            match = self.pattern.match(self.dice_input)

            if not match:
                raise ValueError("Invalid dice notation")

            if match.group(1):
                self.count = int(match.group(1))

            self.sides = int(match.group(2))

            if match.group(3):
                operator_string = match.group(3)
                match operator_string:
                    case '+':
                        operator_func = operator.add
                    case '-':
                        operator_func = operator.sub
                    case '*':
                        operator_func = operator.mul
                    case '/':
                        operator_func = operator.truediv
                self.operator = operator_func

            if match.group(4):
                self.mod = int(match.group(4))
