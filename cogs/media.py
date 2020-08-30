import re
import discord
import requests
from discord.ext import commands

class Media(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def video(self, ctx, *search):
        """Pideme un video de youtube y te lo trearé."""

        if search:
            YOUTUBE_URL = "https://www.youtube.com/"
            YOUTUBE_QUERY_URL = YOUTUBE_URL + "results?search_query = "

            query    = "+".join(search)
            response = requests.get(YOUTUBE_QUERY_URL + query)
            results  = re.findall(r"watch\?v = \S{11}", response.text)

            await ctx.send(YOUTUBE_URL + results[0])

        else:
            await ctx.send("Dime que quieres buscar y te lo traeré, lo prometo!")

def setup(client):
    client.add_cog(Media(client))
