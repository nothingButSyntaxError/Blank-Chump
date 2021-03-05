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

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        act_tim = datetime.datetime.utcnow()
        embed = discord.Embed(title="Thank You!", description=f"Thank you for adding {self.bot.user} to your server!", colour=discord.Colour.gold())
        embed.add_field(name="Setup Instructions", value=f"To setup the bot please do look at the `%help` command and also use the `%setup` command to add your guild to the bots data and so you can use its premium features as well!")
        embed.set_author(name=f"{guild.owner}")
        embed.set_footer(text=f"{act_tim}")
        embed.set_thumbnail(url=guild.owner.avatar_url)
        await guild.owner.send(embed=embed)



def setup(bot):
    bot.add_cog(Functions(bot))