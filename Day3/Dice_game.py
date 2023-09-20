# Roll the dice and it picks the winner!

import random  # module


def roll_dice():
    return random.randint(1, 6)


def dice_game():
    print("Welcome to roll the dice!")  # Displaying a welcome message

    play_game = input("Are you ready to play? (yes/no): ")  # Asking if user is ready to play!

    if play_game.lower() == "no":
        print(f"Goodbye!")
        return 0

    user_name = input("Yay! Whats your name?")
    print(f"Hello, {user_name}, let's play!")

    # Start an infinite loop (until it is ended later by the player)
    while True:
        # Roll the user's score
        user_roll = roll_dice()
        print(f"You rolled a {user_roll}!")

        # Roll the bot's score
        bot_roll = roll_dice()
        print(f"Bot rolled a {bot_roll}!")

        # Compare the scores
        if user_roll > bot_roll:
            print("You won!")

        elif bot_roll > user_roll:
            print("The bot won :(!")

        else:
            print("It was a tie!")

        # Ask if they want to play again
        play_again = input("Would you like to play again? (yes/no)")

        if play_again.lower() == "no":
            break  # End the loop (and the function) when the player decides they've played enough


dice_game()
