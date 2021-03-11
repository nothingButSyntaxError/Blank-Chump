import discord
from discord import user
from discord.ext import commands
import random
import os
import praw

reddit = praw.Reddit(client_id = "98a8P9wKI4LNpA" , 
    client_secret  = "pnBLBmoXkY5WeKGUr5ccNOpRXg" ,
    username = "MainSamarHoon" ,
    password = "Samar123" , 
    user_agent = "reddit10" )

class reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def pewds(self, ctx, member: discord.Member = None):
        subreddit = reddit.subreddit("memes")
        all_subs = []
        top = subreddit.top(limit = 50)
        for submission in top:
        
            all_subs.append(submission)
        random_sub = random.choice(all_subs)
        name = random_sub.title
        url = random_sub.url
        meme_embed = discord.Embed(title=name, colour=discord.Colour.red())
        meme_embed.set_image(url=url)
        await ctx.send(embed=meme_embed)



def setup(bot):
    bot.add_cog(reddit(bot))