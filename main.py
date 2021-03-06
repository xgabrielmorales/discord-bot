import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("---"*20)
    print(f"Has iniciado sesión como: | {client.user.name} - {client.user.id} |")
    print(f"Estás corriendo la versión {discord.__version__} de discord.py")
    print("---"*20)

    activity = discord.Activity(type = discord.ActivityType.listening, name = "R.A.P")

    await client.change_presence(activity = activity)

if __name__ == "__main__":
    print("Cargando los cogs...")

    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            client.load_extension(f"cogs.{filename[:-3]}")

    client.run(os.environ["DISCORD_TOKEN"])
