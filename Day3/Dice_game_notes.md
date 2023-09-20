### Notes for dice game

Importing the random module

```
import random
```

In this first line,  I have imported the random module, which provides functions to generate random numbers.

```
def roll_dice():
    return random.randint(1, 6)
```

Here, I have defined the function, and it uses the `.randint` function to generate a random integer  between 1 and 6 just like a dice. 

```
def dice_game():
    print("Welcome to roll the dice!")

    play_game = input("Are you ready to play? (yes/no): ")
```

This function sets up the entire dice game. 

It starts by printing a welcome message and has an input function that allows user to enter data.

 The user’s response is stored in the variable `play_game`

```
if play_game.lower() == "no":
        print(f"Goodbye!")
        return 0

    user_name = input("Yay! Whats your name?")
    print(f"Hello, {user_name}, let's play!")

```

so I have started off with `‘if ‘` statement to check the user’s input. If the user says no then this message is printed out and by adding the `Return 0` statement, the function can end and the user will not be asked for their name again due to the while loop.

```
while True:
user_roll = roll_dice()
print(f"You rolled a {user_roll}!")

bot_roll = roll_dice()
print(f"Bot rolled a {bot_roll}!")

if user_roll > bot_roll:
    print("You won!")
elif bot_roll > user_roll:
    print("The bot won :(!")
else:
    print("It was a tie!")
```

As I want the game to have a loop, the `while` creates an infinite loop, and it will keep running until a break statement is encountered. 

I have allocated the user and bot values to the `roll_dice` function defined earlier in order to generate a number and print the number allocated for them. 

I have added a `if, elif and else` statement in order to compare the rolls to determine the winner. 

so if the users roll is greater than the bots , the condition is true, and it prints out `You won` to the user.  

if the first condition was not true, then it passes on to the `elif condition` which informs the user that the bot won the round. 

finally, the `else statement`, if none of the conditions were true, it means that the users roll is not greater than the bots , vice versa. Therefore, they must be equal, In this case, the program prints “it was a tie!” to inform the user. 

```
play_again = input("Would you like to play again? (yes/no)")

if play_again.lower() == "no":
    break
```

Finally, here, it's asking the user if they want to play the game again. 

If they say no, the program encounters a `break statement`. So this statement is used to exist the enclosing loop, which in this case is the `while true` loop that controlled this game. 

However, if they type yes, then the game will continue.