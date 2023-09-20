#for in loop to solve fizzbuzz

user = int(input("Enter a number:"))

#checking if user input number is divisible by both 3 and 5
if (user % 3==0 and user % 5==0):
    print ("FizzBuzz")
#checking if number is divisible by 3
elif (user % 3 == 0):
    print ("Fizz")
#checking if number is divisible by 5
elif (user % 5==0):
    print ("Buzz")