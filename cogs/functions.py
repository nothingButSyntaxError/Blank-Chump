import discord
from discord import activity
from discord.abc import _Overwrites
from discord.ext import commands
import os
import datetime
import math
import time

class Functions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print("Ready!")
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="%help"))

   

def setup(bot):
    bot.add_cog(Functions(bot))