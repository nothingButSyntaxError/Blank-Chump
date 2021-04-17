import discord
from discord.ext import commands
import os

class Functions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith == self.bot.user.mention:
            await message.channel.send(f"Hello My name is {self.bot.user}, and my prefix is `%`. Thank you!")

def setup(bot):
    bot.add_cog(Functions(bot))