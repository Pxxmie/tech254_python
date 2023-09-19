# Convert the input string to float
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

# Dividing the height by 100 to convert the cm to m
BMI = weight / (height/100)**2
print("Your BMI is",BMI)

#print statement to state the current health based on BMI
if BMI <= 18.5:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are over weight.")
else:
    print("You are obese.")
