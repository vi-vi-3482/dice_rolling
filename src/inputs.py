import operator


def single_dice():
    while True:
        d = input("Dice size?")
        try:
            d = int(d)
            return d
        except:
            print("Not an integer.")
