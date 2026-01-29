import random
import aiohttp

# async def get_random_pokemon():
    
#     url = "https://pokeapi.co/api/v2/pokemon/?limit=1350"

#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             data = await response.json()
#             all_pokemons = [d['name'] for d in data['results']]
#             random_pokemon = random.choice(all_pokemons)
#             random_pokemon_to_send = random_pokemon.title()
            
#     return random_pokemon, random_pokemon_to_send

# async def get_type_and_img_url(name):
#     url = f"https://pokeapi.co/api/v2/pokemon/{name}"

#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             data = await response.json()
#             pokemon_type = [d['type']['name'] for d in data['types']]
#             url_img = data['sprites']['front_default']
    
#     return pokemon_type, url_img


# asyncio.run(get_random_pokemon)