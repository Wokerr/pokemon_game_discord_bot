import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import aiohttp
from db import create_pool
from utils import get_random_pokemon, get_type_and_img_url

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="w!", intents= intents)

@bot.event
async def on_ready():
    global session
    global pool
    pool = create_pool()
    if not session:
        session = aiohttp.ClientSession()

async def on_close():
    if session and not session.close():
        await session.close()

@bot.command()
async def pokemon(ctx):
    pass
    # pokemon_to_inte, pokemon_to_send = await get_random_pokemon()
    # pokemon_type, pokemon_img_url = await get_type_and_img_url(pokemon_to_inte)
    # print(pokemon_img_url)
    # embed = discord.Embed(title= pokemon_to_send)
    # embed.set_image(url=pokemon_img_url)
    # await ctx.send(embed=embed)

bot.run(os.getenv("BOT_TOKEN"))