# Collections can store multiple pieces of data inside

# Lists - called arrays in other languages

shopping_list =["Salad", "Eggs","Doughnuts", "Milk", "Salmon"]

print(shopping_list)
#print(type(shopping_list))

#print(shopping_list[0]) #Use indexing to find the certain item in the list

shopping_list[2] = "Tomato"
print(shopping_list)

# List Methods

# Add something to the end of a list
shopping_list.append("Carrots")
shopping_list.extend({"water", "Celery"}) #Add multiple
print(shopping_list)


# Remove items from a list

shopping_list.remove("Salad") # Gets rid of any instance of Salad in list.
print(shopping_list)


# pop method - pop you can remove via index but remove you cant

shopping_list.pop() # Removes the last value of the list, when it has nothing passed to it.
print(shopping_list)

shopping_list.pop(1) #Remove a particular index
print(shopping_list)


# Mixed data type lists

mixture = [1, 2,3.0, "one", "two", "three", "four"]
print (mixture)

#List slicing

print (mixture[1:3])
print(mixture[0::2])
print(mixture[::-1]) #print the list backwards




# Tuples- Immutable, they cannot be changed!
# You use Tuples if you do not want a set of values to be overwritten or changed.

essentials = ("bread", "eggs", "milk")

print(essentials)
print(type(essentials))

