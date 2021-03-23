from typing import ValuesView
import discord
from discord import user
from discord import colour
from discord.ext import commands
import random
import os
import traceback

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, *, module):
        try: 
            self.bot.load_extension(f"cogs.{module}")
        except:
            await ctx.send("could not load the module")

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, *, module):
        """Loads a module."""
        try: 
            self.bot.unload_extension(f"cogs.{module}")
        except:
            await ctx.send("could not load the module")

    @commands.command()
    @commands.is_owner()
    async def stc(self, ctx, cog):
        if cog == 'currency':
            await ctx.send("Here is your file:-")
            await ctx.send(file=discord.File("currency.txt"))



def setup(bot):
    bot.add_cog(Admin(bot))
