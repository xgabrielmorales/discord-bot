import os
import discord
from discord.ext import commands

TOKEN = open("TOKEN", mode="r").readline().strip()
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("---"*20)
    print(f"Has iniciado sesión como: | {client.user.name} - {client.user.id} |")
    print(f"Estás corriendo la versión {discord.__version__} de discord.py")
    print("---"*20)
    print("")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("with DOCTYPE"))

if __name__ == "__main__":
    print("Cargando los cogs...")
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            client.load_extension(f"cogs.{filename[:-3]}")

    client.run(TOKEN)
