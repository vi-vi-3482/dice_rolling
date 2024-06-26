from inputs import CLI
from dice import Dice


def main():
    while True:
        cli = CLI()
        cli.input_prompt()

        if cli.string_in == "end":
            break

        elif cli.string_in == "reroll":
            try:
                dice.rolls()
                dice.display_verbose()
                continue
            except UnboundLocalError:
                print("No prior dice rolled, enter one to continue")
                continue

        else:
            prompt_analysis = CLI.BasicRoll(cli.string_in)
            prompt_analysis.read_input()

        dice = Dice(prompt_analysis.count, prompt_analysis.sides, prompt_analysis.operator, prompt_analysis.mod)
        dice.rolls()
        dice.display_verbose()

        print("\nSuccess! \nEnter 'end' to exit \n")
    print("exiting")


if __name__ == "__main__":
    main()
