from dotenv import load_dotenv
import os
import asyncio
import aiomysql
import pymysql
from scripts import get_pokemon_name, get_pokemon_type
from models import Pokemon

load_dotenv()

pokeapi_url = "https://pokeapi.co/api/v2/pokemon/?limit=500"

async def get_pool() -> aiomysql.Pool:
    """
    Creates and returns a connection pool to the database.

    The pool size defaults minsize=1 and maxsize=10.

    Return:
        An instance of aiomysql.Pool
    """
    try:    
        pool = await aiomysql.create_pool(
            host= os.getenv("DB_HOST"),
            user= os.getenv("DB_USER"),
            password= os.getenv("DB_PASSWORD"),
            db= os.getenv("DB_NAME")
        )
        return pool

    except Exception as e: 
        print('Erreor creating pool', e)

def insert_pokemons_names(pokemon_url: str) -> str:
    """
    Create a connection to database.

    Only for pupose to update our database once, for cotidian use choose get_pool() instead.

    Return:
        Confirmation message about database was filled successful
    """

    try:
        conn = pymysql.connect(
            host= os.getenv("DB_HOST"),
            user= os.getenv("DB_USER"),
            password= os.getenv("DB_PASSWORD"),
            database= os.getenv("DB_NAME"),
        )
        print("connection successful")

        
        names = get_name_from_api(pokemon_url)

        cursor = conn.cursor()
        cursor.executemany("INSERT INTO pokemons (pokemon_name) VALUES (%s)", names)
        conn.commit()        

    except Exception as e:
        print("Error trying to connect at db due to:", e)

    finally:
        if conn:
            conn.close()
            cursor.close()

async def get_name_from_api(api_url: str) -> list[str]:
        """
        This parameters is pokeapi where the names will be gathered.
        Return a list with names.
        """
        pokemon_name = get_pokemon_name(api_url)
        names = [(n['name'],) for n in pokemon_name]
        return names


# connection_to_db()


# asyncio.run(get_pool())
# asyncio.run(connection_to_db())

# insert_pokemons_names(pokeapi_url)
