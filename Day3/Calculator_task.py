# Building a simple calculator that can add, subtract, multiply and divide

# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y


# take input from the user
# Display operation menu
print("Please select an operation from below to perform.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

operation = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if operation == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif operation == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif operation == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif operation == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid")
