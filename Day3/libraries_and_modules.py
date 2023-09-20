# Libraries and Modules

# Python has very extensive libraries and modules, this is great for us as DevOps engineers!

# Module = Single file of functions, classes, variables etc. That you can bring in and use in another Python file.

# Library = Collection of modules. Needs to be installed with pip.


import math

num_float = 23.66

print(math.ceil(num_float))  # Round it up
print(math.floor(num_float))  # Rounds it down

import random

rand_list = [1, 2, 3, 4, 5, 6, 7]
print(random.choice(rand_list))  # selects random number from the list

rand_nvm = random.randint(1, 10)  # selecting the number from the range


import requests

request_bbc = requests.get("https://www.bbc.co.uk/")

print(request_bbc.status_code)
print(request_bbc.content)

bbc_content = request_bbc.content