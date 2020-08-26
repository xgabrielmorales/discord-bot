import discord
from discord.ext import commands

class Reactions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        if message_id == 747925275014332486:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)

            # Green Red
            if payload.emoji.name == "🔴":
                role = discord.utils.get(guild.roles, name="Red")
            # Green Blue
            if payload.emoji.name == "🔵":
                role = discord.utils.get(guild.roles, name="Blue")
            # Green Role
            if payload.emoji.name == "🟢":
                role = discord.utils.get(guild.roles, name="Green")
            # Green Yellow
            if payload.emoji.name == "🟠":
                role = discord.utils.get(guild.roles, name="Yellow")

            if role is not None:
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
                else:
                    print("User not found.")
            else:
                print("Role not found.")


    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id
        if message_id == 747925275014332486:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)

            # Green Red
            if payload.emoji.name == "🔴":
                role = discord.utils.get(guild.roles, name="Red")
            # Green Blue
            if payload.emoji.name == "🔵":
                role = discord.utils.get(guild.roles, name="Blue")
            # Green Role
            if payload.emoji.name == "🟢":
                role = discord.utils.get(guild.roles, name="Green")
            # Green Yellow
            if payload.emoji.name == "🟠":
                role = discord.utils.get(guild.roles, name="Yellow")

            if role:
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member:
                    await member.remove_roles(role)
                    print(f"Member {member} has been removed from {role} role.")
                else:
                    print("User not found.")
            else:
                print("Role not found.")

def setup(client):
    client.add_cog(Reactions(client))
