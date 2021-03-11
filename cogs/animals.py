import discord
from discord import user
from discord.ext import commands
import random
import os
import praw

reddit = praw.Reddit(client_id = "98a8P9wKI4LNpA" , 
    client_secret  = "pnBLBmoXkY5WeKGUr5ccNOpRXg" ,
    username = "MainSamarHoon " ,
    password = "Samar123" , 
    user_agent = "reddit10" )

class animals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    @commands.guild_only()
    async def animals(self, ctx, member: discord.Member = None):
        subreddit = reddit.subreddit("animals")
        top = subreddit.top(Limit = 50)
        for submission in top:
            await ctx.send(submission.title)


def setup(bot):
    bot.add_cog(animals(bot))
