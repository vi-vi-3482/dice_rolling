from inputs import CLI
from dice import Dice


def main():
    while True:
        cli = CLI()
        cli.input_prompt()
        if cli.string_in == "end":
            break

        prompt_analysis = CLI.BasicRoll(cli.string_in)
        prompt_analysis.read_input()

        dice = Dice(prompt_analysis.count, prompt_analysis.sides, prompt_analysis.operator, prompt_analysis.mod)
        dice.rolls()
        dice.display_rolls()

        print("Success! \nEnter 'end' to exit")


if __name__ == "__main__":
    main()
