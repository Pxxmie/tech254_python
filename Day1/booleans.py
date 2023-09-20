# What is a Boolean?

# Binary option between True or False.

a = True
b = False

print (a == b)# is a equal to b
print (a != b)# is a not equal to b
print(a >= b) # is a greater than b
print(a <=b) # is a less than b

# Logical/Comparison operators always give back True or False.

print (2 > 1)

print(True and False) # False
print(True or False)# True


# Boolean methods

hi = "Hello world!"

print(hi.isalpha()) #checking if its alphabetical characters

print(hi.islower())

print(hi.endswith("!")) #checking if the words ends with

print(hi.startswith("Hello"))



# Boolean values

x = 0
y = 10

print(bool(x)) # x=0 false = 0
print(bool(y)) # y = 10 , any value thats not 0 is true



# Value of None (null in other languages)
#User as a placeholder value  - list or dictionary

z = None
t = True

print(bool(z))
print(z == False)
print(z == None) # not best practice
print( z is None) # Best practice
print(z is not None)

print(type(z))
print(type(t))

