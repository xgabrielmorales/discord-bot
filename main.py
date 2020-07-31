import os
import discord
from discord.ext import commands

TOKEN = ""
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("---"*20)
    print(f"Has iniciado sesión como: {client.user.name} - {client.user.id}")
    print(f"Estás corriendo la versión {discord.__version__} de discord.py")
    print("---"*20)
    print("")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("with DOCTYPE"))

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    print("Casí pero no")

    if message_id == 738157656535072836: 
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

if __name__ == "__main__":
    print("Cargando los cogs...")
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                client.load_extension(f"cogs.{filename[:-3]}")
            except Exception as error:
                print(f"{extension} no se pudo iniciar [{error}]")

    client.run(TOKEN)
