# what are operators?

# Symbols that execute a particular mathematical or logical function.

# Arithmetic operators:
# +, -, *, /, %.

# Logical (Comparison) operators:
# >, <, ==,!=,>=, <=

# Numeric Types

# int(whole numbers), float(1.01, 23.5), complex

a = 24
b = 16

print(a +b)
print(a > b)

a = 16.5
b = 24

print (a > b)
print (a + b)

# one_third = 1 / 3
# print (one_third)
# print(one_third * 3) #by default Python rounds it up.

# Strings
single_quotes = 'Look! Single quotes'
double_quotes = "Look! 'Double quotes'" #most preferred

print(double_quotes)

# string slicing

# H e l l o  W o r l d !
# 0 1 2 3 4 5  6 7 8 9 10 11
#

hw = "Hello World!"

print(hw[6:])
print(hw[0:5])
print(hw[-5:]) #minus indexing
print(hw[-0])

# String Methods

strip_string = "Hi my name is Prismika           "
print(len(strip_string))
print(len(strip_string.strip()))  # gets rid of the white spaces and beginning and end of string

example_text = "Here's some text with lot's of text"

print(example_text.count("text"))# counts sets of characters in string
print(example_text.lower()) #Turns characters into lowercase
print(example_text.capitalize())
print(example_text.replace("with", ",")) #replaces


# Casting

a = 2
b = 5.4
c = "3"

# print(a + b + c) # you cannot add string together with numeric
print(a + b + int(c)) # casting
print(float(c))



# Concatenation

# Adding strings altogether

d = " theres now a number 25.4 unless we put a space in"

print(str(a) +"," + str (b) + d)

# f-strings
# f stands for format

name = "Prismika"
years = 26
height_cm = 152.6

print(f"{name} is {years} years old and {height_cm}cm tall")

snoop = "Snoopy"
snoop_years = 40

print(f"{name.upper()} IS {snoop_years  *7} YEARS OLD IN DOG YEARS!")



# Rounding

# pi = 3.14159265359

# print(f"Pi to 3 decimal places: {pi:.3f}") # 3.142
# print(f"Pi to 5 decimal places: {pi:.5f}") # 3.14159



# Percentages

score = 16
max_score = 26

print(f"You scored {score/max_score}")
print(f"You scored {score/max_score:%}")
print(f"You scored {score/max_score:.2%}")
print(f"You scored {score/max_score:.0%}")


# Modulo
print (10 / 3) # decimal
print (10 % 3) # whole number

x = 6
y = "Pris"
print (x)
print (y)


