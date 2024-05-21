import random
import inputs


def single_roll(d: int) -> int:
    rolled = random.randrange(d)
    return rolled


def main():
    d = inputs.single_dice()
    rolled = single_roll(d)
    print(f"You rolled a d{d} and got {rolled}")


if __name__ == "__main__":
    main()
