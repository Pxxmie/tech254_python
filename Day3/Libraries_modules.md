
## Libraries and Modules

### What are Modules?

A module is a  file containing Python functions, classes, variables, statements with the `.py` extension. The use of modules make it easier to read the code as it breaks it into manageable pieces. 

Example: 

```python
import math

num_float = 23.66

print(math.ceil(num_float))  # Round it up
print(math.floor(num_float))  # Rounds it down
```

In this example, we have instructed Python to import the `math`library which contains a set of  mathematical functions which are modules.  Using the `math.ceil` function takes the value in `num_float` and rounds it up to the nearest whole number. So 23.66 is rounded up to 24. 

Another math function we have used is `math.floor`, which takes the value in `num_float` and rounds it down to the nearest whole number. So 23.66 is rounded down to 23.

Output: 

```python
24
23
```

### What are libraries?

A library is a collection of pre-written code(modules). For example the math library provides functions for mathematical operations, and the random library provides functions for generation random numbers. We can use libraries to access a wide range of functionalities that other developers have already used and tested. 

Example: