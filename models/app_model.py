from pydantic import BaseModel
from datetime import datetime

### USER MODEL ###

class User(BaseModel):
    guild_id: int # This must be a server ID in discord
    user_id: int # This must be a discord ID

### POKEMON MODEL ###

class Pokemon(BaseModel):
    pokemon_name: str

class Type(BaseModel):
    type: str

### POKEDEX MODEL ###

class Pokedex(BaseModel): # Here's where the pokemon will saved with discord ID of his owner
    user_id: int # Relationship between User and Pokedex
    pokemon_id: int # Relationship between Pokemon and Pokedex
    capture_date: datetime # Moment where the pokemon was picked up

