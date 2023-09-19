## Python Fundamentals 

### Data Types

Python has the following data types built-in by default, in these categories: 

- **Text Type**: str
- **Numeric Types**: int (1, 365), float( 45.6, 30.0), complex 
- **Sequence Types**: list, tuple 
- **Mapping Type**: dictionary
- **Set Types**: set, frozensets 
- **Boolean Types**: bool 

### Getting the Data Type

You can get the data type of any object by using the `type ()` function: 

Example
```python
x = 5 
print (type(x))
```
The output will show 
`<class 'int'>` to tell us that `x` is an **int**.

### Variables 
A variable is created the moment you first assign a value to it. 
Example 

```python
x = 6
y = "Pris"
print (x) 
print (y)
```
The output will show; 
<br>
`6` 
<br>
`Pris`

### Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks .
<br>
`'hello'` is the same as `"hello"`.

### String Slicing 
You can return a range of characters by using the slice syntax. 
Specify the start index and the end index, separated by a colon, to return a part of the string. 

Example 

```python
hw = "Hello World!"

print(hw[6:])
print(hw[0:5])
print(hw[-5:])# Minus indexing
print(hw[-0])

```
The output will show:
```
World!
Hello
orld!
H
```

### String Concatenation 
To concatenate, or combine, two strings you can use + operator. 

Example 
Merge a with variable b into variable c, to add a space between them, add a " " :
```python
a = "Hello"
b = "World"
c = a + " " + b
print(c)
```
The output will show: 
```
Hello World
```
### Format Strings
We can combine strings and numbers by using the format () method! <br>
The format () method takes the passed arguments, formats them, and places them in the string where the placeholder {} are:

Example

```python
name = "Prismika"
years = 26
height_cm = 152.6

print(f"{name} is {years} years old and {height_cm}cm tall")


snoop = "Snoopy"
snoop_years = 40

print(f"{name.upper()} IS {snoop_years  *7} YEARS OLD IN DOG YEARS!")

```
The output will show: 
```commandline
Prismika is 26 years old and 152.6cm tall

PRISMIKA IS 280 YEARS OLD IN DOG YEARS!
```

### String Methods 

Python has a set of built-in methods that you can use on strings. 

#### Upper Case
The upper() method returns the string in upper case: 
```python
a = "Hello, World!"
print(a.upper()) 

```
The output will show: 
```
HELLO, WORLD!
```
#### Lower Case
The lower() method returns the string in lower case: 
```python
a ="Hello, World!"
print(a.lower())
```
The output will show: 

```
hello, world!
```
#### Replace String 
The replace() method replaces a string with another string: 
```python
a ="Hello, World!"
print(a.replace("H","J"))
```
The output will show: 
```
Jello, World!
```

#### Strip String 

The strip() method removes any leading, and trailing whitespaces.

Leading means at the beginning of the string, trailing means at the end.

You can specify which character(s) to remove, if not, any whitespaces will be removed.
<br>
<br>
Example:
```python
strip_string = "Hi my name is Prismika           "
print(len(strip_string))
print(len(strip_string.strip()))  # gets rid of the white spaces and beginning and end of string
```











