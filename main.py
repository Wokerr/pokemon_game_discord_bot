# import discord
# from discord.ext import commands
# from dotenv import load_dotenv
# import os
# from apitest import test1
# from db import insert_pokemons_names

# load_dotenv()

# intents = discord.Intents.default()
# intents.message_content = True

# bot = commands.Bot(command_prefix="w!", intents= intents)

# @bot.event
# async def on_ready():
#     print(f'Logged in as {bot.user}!')  

#     # channel = bot.get_channel(839668007621361704)
#     # await channel.send("El mejor bot a despertado mi gente")

# # @bot.command()
# # class Client(discord.Client):
# #     async def on_ready(self):
# #         print(f"Logged in as {self.user}!")

# #     async def on_message(self,message):
# #         if message.author == self.user:
# #             return
        
# #         if message.content == "!ping":
# #             await message.channel.send("Soy la mera verga mi compa")
        
# #     async def evan(self):

# # @bot.command()
# # async def test(ctx):
# #     await ctx.send(test1)



# bot.run(os.getenv("BOT_TOKEN"))

insert_pokemons_names("https://pokeapi.co/api/v2/pokemon/?limit=1350")