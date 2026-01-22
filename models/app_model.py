from pydantic import BaseModel
from datetime import datetime

### USER MODEL ###

class User(BaseModel):
    user_id: int # This must be a discord ID

### POKEMON MODEL ###

class Pokemon(BaseModel):
    pokemon_id: int
    pokemon_name: str
    pokemon_type: str

### POKEDEX MODEL ###

class Pokedex(BaseModel): # Here's where the pokemon will saved with discord ID of his owner
    id: int
    user_id: int # Relationship between User and Pokedex
    pokemon_id: int # Relationship between Pokemon and Pokedex
    capture_date: datetime # Moment where the pokemon was picked up

