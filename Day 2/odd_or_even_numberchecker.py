# to check if the input number is odd or even
num = int(input("Enter a number: "))
#if a number is divisable by 2 then it is even. Using the remainder operator % helps us calculate the remainder. if the remainder is not 0 then it is a odd number.
mod = num % 2

# if the remainder is greater than 0 then it's an odd number
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")