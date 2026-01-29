from pydantic import BaseModel
from datetime import datetime

### USER MODEL ###

class User(BaseModel):
    user_id: int # This must be a discord ID

### GUILD MODEL ###

class Guild(BaseModel):
    guild_id: int

### POKEMON MODEL ###

class Pokemon(BaseModel):
    pokemon_name: str
    pokemon_id: int


