# passing is making something [more] understandable. So it makes json more understandable for Python.

import json

parsed_json = json.loads(open('example_json.json').read())
value = parsed_json["name"] # variable
print(value)


# past_json = variable

# .loads - using the module inside json - it converts the json string into python dictionary for you.
# .load - just reads the content.

# open - in built python -opens the file

# .read - reads the content within the open file and turns the json string content into a python string
