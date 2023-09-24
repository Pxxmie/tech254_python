# API requests

import requests
import json

post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

print(post_codes_req)
print(post_codes_req.headers)  # gives the headers
print(post_codes_req.content)  # gives json body as bytes



#Long way
# post_codes_dict = json.loads(post_codes_req.content)  # turns it into python dict
# print(type(post_codes_dict))


#Short way
print(post_codes_req.json())
