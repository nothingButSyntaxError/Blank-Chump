import discord
from discord import user
from discord.ext import commands
import random
import os

class games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.command()
 @commands.guild_only()
async def rps(self, ctx, member: discord.Member = None):


def setup(bot):
    bot.add_cog(games(bot))