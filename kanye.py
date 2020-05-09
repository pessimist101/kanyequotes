import aiohttp
import discord
from discord.ext import commands
import json


class Kanye(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Kanye cog online')

    # Commands
    @commands.command()
    async def kanye(self, ctx):
        async with aiohttp.ClientSession() as session:
            data = await session.get('https://api.kanye.rest')
            data = await data.json()
            quote = data['quote']
        embed = discord.Embed(colour=discord.Colour(0x4169e1), description=quote)
        await ctx.message.delete()
        await ctx.send(embed)

def setup(client):
    client.add_cog(Kanye(client))