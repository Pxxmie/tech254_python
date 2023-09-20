# Importing random library which will generate random numbers
import random


# def defines a function named con_flip, and we use random.choice to randomly select Heads or tails.
def coin_flip():
    # It chooses either heads or tails and assigns it to the variable 'result'
    result = random.choice(["Heads", "Tails"])
    # it then sends back the result of the coin flip to the function.
    return result


# stores the result in the variable 'flip_result'
flip_result = coin_flip()

# prints out the result of the coin flip
print(f"You got {flip_result}!")
