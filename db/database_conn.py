from dotenv import load_dotenv
import os
import asyncio
import aiomysql

load_dotenv()

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
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            db=os.getenv("DB_NAME")
        )
        return pool

    except Exception as e: 
        print('Erreor creating pool', e)

asyncio.run(get_pool())
