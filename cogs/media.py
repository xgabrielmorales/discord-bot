import re
import discord
from discord.ext import commands
from urllib import parse, request

class Media(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def video(self, ctx, *, search):
        """Pideme buscar un video en youtube con el comando !video y te lo trearé.""" 

        query_string = parse.urlencode({'search_query': search})
        html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
        search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())

        await ctx.send("https://www.youtube.com/watch?v=" + search_results[0])

def setup(client):
    client.add_cog(Media(client))
