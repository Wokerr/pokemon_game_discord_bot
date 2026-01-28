import requests
import aiohttp


# url = "https://pokeapi.co/api/v2/pokemon/?limit=500"

# with requests.get(url) as data:
#     poke = data.json()
#     pokemon_name = [p['name'] for p in poke['results']]
#     print(pokemon_name)

url_type_pokemons = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_name(api_url: str) -> str:
    """
    Docstring for get_pokemon_name
    
    :param api_url: Base URL where information is obtained
    :type api_url: str
    :return: Description
    :rtype: str

    """
    with requests.get(api_url) as data:
        response = data.json()
        pokemon_name = response['results']

        return pokemon_name

def get_pokemon_type(api_url: str) -> list[str]:
    """
    Docstring for get_pokemon_name
    
    :param api_url: Base URL where information is obtained
    :type api_url: str
    :return: Description
    :rtype: str

    """
    data = requests.get(api_url)
    response = data.json()
    pokemon_type = [type['type']['name'] for type in response['types']]

    return pokemon_type

# print(get_pokemon_type("https://pokeapi.co/api/v2/pokemon/4"))
