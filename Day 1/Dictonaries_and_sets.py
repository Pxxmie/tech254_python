# What is dictionary?

# Uses key/value pairs
# Key = the reference to the object
# Value = the data storage mechanism you want to use (varaiable, list, dictionary etc.)

# Making a Dictionary

student_1 = {
    "name": "Prismika",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data_types", "operators"]
}

print(student_1)

# Accessing data using the key(s)

print(student_1["stream"])
print(student_1["completed_lesson_names"][0])

# Changing a value in a dict

student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])

#Removing
student_1["completed_lesson_names"].remove("data_types")
print(student_1["completed_lesson_names"])

# Getting the keys

print(student_1.keys())


# Sets and Frozen sets

# No order to the collection. It's in a random order.
# You cannot have duplicated items in a set

car_parts = {"wheels", "doors", "exhaust", "windows"}
print (car_parts)

car_parts.add("steering_wheel") #add to the set
print(car_parts)

car_parts.discard("windows") # remove from the set
print(car_parts)

# Frozen Sets- immutable set ( cannot be changed)

x = frozenset ([1, 2, 3, 4,5,])
print (x)