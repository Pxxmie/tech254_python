# Functions

# DRY - Don't Repeat Yourself

# Allow us to embed/reference code, making it reusable.

# Making a function


# colon is needed as we are going to attribute code after this colon
def print_something(print_string):  # print_string is a placeholder variable-this turns it into an argument.
    print(print_string)


print_something("We can pass anything in here!")
print_something("Like this!")


# print string is not a global variable.

# using f string on function
def greeting(name):
    print(f"Hello, my name is {name}")


greeting("Pris")


# the return statement-good practice then print statement
# return statement is holding a value for example (int1, int2) returned from doing that function.

def addition(int1, int2):
    return int1 + int2


print(addition(2, 2))


# default arguments

def addition(int1=2, int2=4):
    return int1 + int2


# print(addition(5, 5))
# print(addition(10, 15))


# multiple arguments

def multi_args(*multiargs):  # multi_arg is a function, *multiargs is tuple.
    # the star allows you to provide as much information as you want.
    for arg in multiargs:  # looping through the tuple and print out each individual element
        print(arg)
    # print(type(multiargs))


multi_args(1, 2, 3, 4, 5, "six")

# Look into type hints-how to do it and how to put that in?


# Function good practices

# comment the functions-adding useful comments to explain your functions.
# Clear function names and clear function argument names.
# Keep your functions small and compact. (improves readability)- Make them do one thing if possible.
# Avoiding duplication
# Correct indentation and formatting/syntax.
# Function should be organised properly.
# Do not use function unnecessarily.
# Functions at the start of your code if possible.
# Remember the return statement! (good habit)
# Consider using type hints.

