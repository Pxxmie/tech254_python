# While loops

# For Loops are all to do with iterating through a collection
# While Loops are more like a monitor > while something is true then act. People use while loop so they want the program running.

x = 0

while x < 10:
    print(f"It's working -->{x}")
    if x == 4: #it stops when x is 4 and it breaks out the while loop
        break
    x += 1

# verifying user input

user_prompt = True

while user_prompt:
    age = input("What is your age?")
    if age.isdigit() and int(age) <118:#this allows user to input digit instead of alphabetic characters as well as verifiying the age
        user_prompt = False
    else:
        print("Please provide your answer in digits, below 118")

print(f"Your age is {age}")

# I made a change


