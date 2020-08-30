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

        if message_id == 749516015284781068:
            if payload.emoji.name == "👨‍🌾":
                role   = discord.utils.get(guild.roles, name = "Proletariado")
                member = discord.utils.find(lambda member: member.id == payload.user_id, guild.members)

                await member.add_roles(role) if member else print("User not found")
        if message_id == 749517027479388243:
            if payload.emoji.name == "🐧": # Pinguino
                role = discord.utils.get(guild.roles, name = "Dev")

            if role:
                member = discord.utils.find(lambda member: member.id == payload.user_id, guild.members)
                await member.add_roles(role) if member else print("User not found")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)

        if message_id == 749516015284781068:
            if payload.emoji.name == "👨‍🌾":
                role   = discord.utils.get(guild.roles, name = "Proletariado")
                member = discord.utils.find(lambda member: member.id == payload.user_id, guild.members)

                await member.remove_roles(role) if member else print("User not found")

        if message_id == 749517027479388243:
            if payload.emoji.name == "🐧": # Pinguino
                role = discord.utils.get(guild.roles, name = "Dev")

            if role:
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                await member.remove_roles(role) if member else print("User not found")
            else:
                print("Role not found.")

def setup(client):
    client.add_cog(Reactions(client))
