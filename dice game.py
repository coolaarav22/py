import random


def roll_dice():
    return random.randint(1, 6)


def play_dice_game():
    print("Welcome to the Dice Rolling Game!")
    while True:
        user_input = input("Press Enter to roll the dice, or type 'quit' to exit: ").lower()
        if user_input == 'quit':
            print("Thanks for playing!")
            break
        elif user_input == '':
            die1 = roll_dice()
            die2 = roll_dice()
            print(f"You rolled a {die1} and a {die2}. Total: {die1 + die2}")
        else:
            print("Invalid input. Please press Enter or type 'quit'.")


            if __name__ == "__main__":
               play_dice_game()