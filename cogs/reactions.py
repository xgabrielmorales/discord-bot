import discord
from discord.ext import commands

class Reactions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)

        if message_id == 748146277140922400:
            if payload.emoji.name == "👨‍🌾":
                role   = discord.utils.get(guild.roles, name="Proletariado")
                member = discord.utils.find(lambda member: member.id == payload.user_id, guild.members)

                await member.add_roles(role) if member else print("User not found")

        if message_id == 748157275893530684:
            print(payload.emoji.name)
            if payload.emoji.name == "🔴": # Red Role
                role = discord.utils.get(guild.roles, name="Red")
            if payload.emoji.name == "🔵": # Blue Role
                role = discord.utils.get(guild.roles, name="Blue")
            if payload.emoji.name == "🟢": # Green Role
                role = discord.utils.get(guild.roles, name="Green")
            if payload.emoji.name == "🟡": # Yellow Role
                role = discord.utils.get(guild.roles, name="Yellow")

            if role:
                member = discord.utils.find(lambda member: member.id == payload.user_id, guild.members)
                await member.add_roles(role) if member else print("User not found")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)

        if message_id == 748146277140922400:
            if payload.emoji.name == "👨‍🌾":
                role   = discord.utils.get(guild.roles, name="Proletariado")
                member = discord.utils.find(lambda member: member.id == payload.user_id, guild.members)

                await member.remove_roles(role) if member else print("User not found")

        if message_id == 748157275893530684:
            if payload.emoji.name == "🔴": # Red Role
                role = discord.utils.get(guild.roles, name="Red")
            if payload.emoji.name == "🔵": # Blue Role
                role = discord.utils.get(guild.roles, name="Blue")
            if payload.emoji.name == "🟢": # Green Role
                role = discord.utils.get(guild.roles, name="Green")
            if payload.emoji.name == "🟡": # Yellow Role
                role = discord.utils.get(guild.roles, name="Yellow")

            if role:
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                await member.remove_roles(role) if member else print("User not found")
            else:
                print("Role not found.")

def setup(client):
    client.add_cog(Reactions(client))
