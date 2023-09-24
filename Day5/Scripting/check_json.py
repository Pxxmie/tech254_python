# script to check an example_json.json file

import json
import os
import sys

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):  # checking if the file exists.
        file = open(sys.argv[1], "r")  # r stands for read only
        json.load(file)  # using load instead of loads as we only want to check/ read data.
        file.close()
        print("JSON is VALID!")

    else:
        print(sys.argv[1] + " not found")

else:
    print("Usage: python check_json.py <file>")

# on git bash terminal, you type  python check_json.py example_json.json
