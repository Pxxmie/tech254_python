import requests
import json

# Get the list of Pokémon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']

# Ask the user to choose a Pokémon
print('Player 1 enter your Pokémon:')
choice = input().lower()

# Get the Pokémon's data from the API
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(choice)
response = requests.get(url)
pokemon_data = json.loads(response.text)

# to get ability
abilities = pokemon_data['abilities'][0]
ability = abilities['ability']

# to format height and weight properly
height = int(pokemon_data['height'])
weight = int(pokemon_data['weight'])

height_formatted = height / 10
weight_formatted = weight / 10

# Ask play 2 to choose Pokémon
print('Player 2 enter your Pokémon:')
p2_choice = input().lower()

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(p2_choice)
p2response = requests.get(url)
p2pokemon_data = json.loads(p2response.text)

# to get ability
p2_abilities = p2pokemon_data['abilities'][0]
p2ability = p2_abilities['ability']

# to format height and weight properly
p2height = int(p2pokemon_data['height'])
p2weight = int(p2pokemon_data['weight'])

p2height_formatted = p2height / 10
p2weight_formatted = p2weight / 10

poke1_strength = weight_formatted * height_formatted
poke2_strength = p2weight_formatted * p2height_formatted

# Test code for winners if statement
# print(poke2_strength)
# print(poke1_strength)

if poke1_strength > poke2_strength:
    print("Player One Wins!!!")
else:
    print("Player Two Wins!!!")
