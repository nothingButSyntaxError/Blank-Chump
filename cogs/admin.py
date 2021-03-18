<<<<<<< HEAD:cogs/admin.py
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
        """Loads a module."""
        try: 
            self.bot.load_extension(module)
        except:
            await ctx.send("could not load the module")

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, *, module):
        """Loads a module."""
        try: 
            self.bot.unload_extension(module)
        except:
            await ctx.send("could not load the module")

def setup(bot):
=======
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
        """Loads a module."""
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

def setup(bot):
>>>>>>> 57cdea4e508fc28c8bbce0f0ff9cc2d5824957bb:admin.py
    bot.add_cog(Admin(bot))