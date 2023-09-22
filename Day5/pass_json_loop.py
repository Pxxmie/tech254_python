import json
parsed_json = json.loads(open('example_json.json').read())

for key, value in parsed_json.items():
    print(f"{key}, {value}")
