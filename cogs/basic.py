import discord
from discord.ext import commands

url_twitch = "https://www.twitch.tv/xgabrielmorales"

class Basic(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def info(self, ctx):
        """Reglas e información del servidor."""

        embed = discord.Embed(
            title = f"!Hola!",
            description = f"Bienvenida/o a este server hecho para la comunidad de xGabrielMorales en Twitch!",
            colour = discord.Colour.green()
        )

        embed.add_field(
            name = "Reglas",
            value = "Sé siempre respetuosa/o y educada/o.\n No se tolera el acoso ni el spam.\n Es de mal gusto escribir en mayusculas.",
            inline = True
        )

        embed.add_field(
            name = "Fecha de creación",
            value = "28/Jul/2020",
            inline = True
        )

        embed.add_field(
            name = "Roles",
            value = "¡Sé parte del proletariado! Reacciona a este mensaje con un :man_farmer: para acceder a otros canales.",
            inline = False
        )

        await ctx.send(embed = embed)

    @commands.command()
    async def dev(self, ctx):
        """Info acerca del rol de dev."""

        embed = discord.Embed(
            title = "¿Te gusta la programación?",
            description = "¡Reacciona a este mensaje con un :penguin: y accede a los canales para ello!",
            colour = discord.Colour.green()
        )

        await ctx.send(embed = embed)

    @commands.command()
    async def twitch(self, ctx):
        """Obten información acerca de mi Twitch."""

        embed = discord.Embed(
            title = "Unete a mi Twitch",
            description = f"Recuerda que puedes seguirme en [Twitch]({url_twitch}) para no perderte ningun stream!",
            colour = discord.Colour.blue()
        )

        await ctx.send(embed = embed)

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, amount = 10):
        """Limpia el historial de mensajes"""
        await ctx.channel.purge(limit = amount)

def setup(client):
    client.add_cog(Basic(client))
