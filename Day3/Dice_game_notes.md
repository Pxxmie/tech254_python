
### Notes for dice game

Importing the random module

```
import random

def roll_dice():
    return random.randint(1, 6)
```

In this first line,  I have imported the random module, which provides functions to generate random numbers.

Here, I have defined the function, and it uses the `.randint` function to generate a random integer  between 1 and 6 just like a dice. 

```
def dice_game():
    print("Welcome to roll the dice!")

    play_game = input("Are you ready to play? (yes/no): ")
```

This function sets up the entire dice game. 

It starts by printing a welcome message and has an input function that allows users to state whether they want to play.

 The user’s response is stored in the variable `play_game`

```
if play_game.lower() == "no":
        print(f"Goodbye!")
        return 0

    user_name = input("Yay! Whats your name?")
    print(f"Hello, {user_name}, let's play!")

```

 I have started off with `‘if ‘` statement to check the user’s input. If the user says no then the goodbye message is printed. By adding the`return 0` statement inside the if body, the function terminates, which means the user will be not asked for their name etc.

Otherwise, It  prompts the user to enter their name. The print statement has an f string calling the `user_name` variable.

```
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
```

As I want the game to loop until the player chooses to stop playing, the `while True` creates an infinite loop that will keep running until a break statement is encountered. 

I have assigned the `user_roll` and `bot_roll` variables to the `roll_dice` function defined earlier to generate a random number for each. These numbers are printed for user to see.

I have added an `if, elif and else` statement to compare the rolls and determine the winner. 

So, if the user roll is greater than the bot, the condition is true, and it prints out `You won!` to the user.  

If the first condition was not true, then it passes on to the `elif statement` which, if true, informs the user that the bot won the round. 

Finally, if none of the conditions were true, it means that the user roll is not greater than the bots and vice versa. Therefore, they must be equal, In this case, the program prints `it was a tie!` to inform the user. 

```
play_again = input("Would you like to play again? (yes/no)")

if play_again.lower() == "no":
    break
```

Finally, here, I added an input asking the user if they want to play the game again. 

If they say no, the `break statement` terminates the while loop. 

However, if they type yes, then the game will continue.