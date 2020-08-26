import discord
from discord.ext import commands

url_twitch = "https://www.twitch.tv/xgabrielmorales"

class Basic(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def info(self, ctx):
        """Server info and rules. Don't break the rules little bitch"""

        embed = discord.Embed(
            title = f"!Hola!",
            description = f"Bienvenido a este server hecho para la comunidad de xGabrielMorales en Twitch!",
            colour = discord.Colour.green()
        )

        embed.add_field(
            name = "Reglas",
            value = "Sé siempre respetuoso y educado.\n No se tolera el acoso ni el spam.\n Es de mal gusto escribir en mayusculas.",
            inline=True
        )

        embed.add_field(
            name = "Fecha de creación",
            value="28/Jul/2020",
            inline=True
        )

        await ctx.send(embed = embed)

    @commands.command()
    async def twitch(self, ctx):

        embed = discord.Embed(
            title = "Unete a mi Twitch",
            description = f"Recuerda que puedes seguirme en [Twitch]({url_twitch}) para no perderte ningun stream!",
            colour = discord.Colour.green()
        )

        await ctx.send(embed = embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount = 10):
        await ctx.channel.purge(limit=amount)

def setup(client):
    client.add_cog(Basic(client))
