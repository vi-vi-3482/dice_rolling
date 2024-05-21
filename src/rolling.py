import random
import inputs


def roll(d):
    rolled = random.randrange(d)
    return rolled


def main():
    d = inputs.single_dice()
    rolled = roll(d)
    print(f"You rolled a d{d} and got {rolled}")


if __name__ == "__main__":
    main()