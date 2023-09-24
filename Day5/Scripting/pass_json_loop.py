# This imports the json module
import json

# This line loads and parses the content of the file example_json.json into a Python dictionary. json.loads() takes a JSON string and converts it to a Python structure.
parsed_json = json.loads(open('example_json.json').read())

for key, value in parsed_json.items():  # returns a sequence of (key, value) pairs in the dictionary.
    print(f"{key}, {value}")
    

# another way to do a loop
# for key in json:
# value = json[key]
# print ("The key and value are ({}) = ({})".format(key, value))
