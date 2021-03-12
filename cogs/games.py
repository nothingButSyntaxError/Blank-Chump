import discord
from discord.ext import commands
import os
import random


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Games(bot))