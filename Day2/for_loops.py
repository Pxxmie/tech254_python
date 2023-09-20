# For Loops
# Python uses 'for' only, no 'for each' loops

list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4,5,6]]
#dic needs keys
dict_data = {
    1: {"name": "Prismika",
        "money": "£0.05"},
    2: {"name": "Masha",
        "money": "£3.66"},
    3: {"name": "Roscoe",
        "money": "£1.50"}
}
# num is a variable name- num stands for all the indexes in the list_data (1,2,3,4,5).
for num in list_data:
    print(num * 2)

# nested for loops

for data in embedded_lists:
    print(data)
    #print whats currently inside data.
    for num in data:
        print(num)

# looping through dictionaries

for value in dict_data:
    print(value)

#prints out the values inside the dic
for item in dict_data.values():
    print(item)
#iterating thorough the value
for item in dict_data.values():
    for embed_value in item.values():
        print(embed_value)

# get value for individual keys

for items in dict_data.values():
    print(items["money"])

#Loops and If statements

for num in list_data:
    if num == 3:
        print("I found 3!")
    elif num > 3:
        print("Gone too far!")
    else:
        print("Too soon!")
