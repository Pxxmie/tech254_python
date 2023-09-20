# Day3 Notes

## Functions

A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

A function is defined using the `def` keyword:

Example

```python
def print_something():  
    print(print_string)
     
```

### Arguments

Information can be passed into functions as arguments. 

Arguments are specified after the function name, inside the **parentheses ().** You can add as many arguments as you want, however you need to separate them with a comma. 

Example below has a function with one argument (print_string). it then uses the ‘print’ function to output the value of the ‘print_string’ variable. 

```python
def print_something(print_string):  # print_string is a placeholder variable- this turns into an argument. 
# colon is needed as we are going to attribute code after this. 
    print(print_string)
     

print_something("We can pass anything in here!")
print_something("Like this!")
```

Another example of an argument using **f string** on a function:

```python
def greeting(name):
    print(f"Hello, my name is {name}")

greeting("Pris")
```

In this example, we define a function called ‘greeting’ that takes one argument (name). Inside the function, we use an f-string to create a message that incorporates the (name) variable. 

Output: 

```python
Hello, my name is Pris
```

### Return Statement

The `return` keyword is to exit a function and return a value.

Using a return statement in a function is good practice because it allows the function to provide a specific result back to the part that called it. This makes the code more organised and easier to understand. 

Example: 

```python
def addition(int1=2, int2=4):
    return int1 + int2

print(addition(5, 5))
print(addition(10, 15))
```

In this example, this code defines a function called `addition` .The function takes two inputs, `int1` and `int2`. These are numbers that we can use in our calculations. The `=2` and `=4` means that if you do not provide any values when you run the function, it will use 2 for ‘int1’ and 4 for ‘int 2’ as default values instead of returning ‘None’.

`print(addition(5, 5))` is calling the addition function with `5` as `int1` and `5` as `int2,` this then calculates 5 +5 which is 10. This result is then printed. 

Output:

```python
10
25
```

### Multiple Arguments

This example below shows the code defines a function named `multi_args,` which takes in a variable number of arguments `(*multiargs”`). It then iterates through each argument and prints it along with the type of ‘multiargs’.

When you call `‘multi_args(1, 2, 3, 4, 5,”six”)’`,  you are passing six arguments to the function. 

`arg` takes on each value in `“multiargs”` one by one, so it starts with 1 and end with “six”. The `“print(arg)”` statement prints the value of `“arg”` on the console. 

The `print(type(multiarge))` statement prints the type of `multiargs`, which is always <class ‘tuple’> because `*multiagrs` collects the arguments into a tuple. 

```python
def multi_args(*multiargs): 
    for arg in multiargs: 
        print(arg)
    # print(type(multiargs))

multi_args(1, 2, 3, 4, 5, "six")
```

Output: 

```python
1
2
3
4
5
six
```