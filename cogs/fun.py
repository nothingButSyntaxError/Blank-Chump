import discord
from discord.ext import commands
import os
import random


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def google(self, ctx, term):
        link = f"http://lmgtfy.com/?q={term}"
        embed = discord.Embed(title="LMGTFY", url=f"https://lmgtfy.com/?q={term}", description="Cant do anything more than this find your query by going on this link lazy idiot!")
        await ctx.send(link, embed=embed)

    @google.error
    async def google_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You have to send what you want to google with the command!")


def setup(bot):
    bot.add_cog(Fun(bot))