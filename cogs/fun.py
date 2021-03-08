import discord
from discord.ext import commands
import os
import random


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def google(self, ctx, term):
        link = f"http://lmgtfy.com/?q={term}"
        embed = discord.Embed(title="LMGTFY", url=f"https://lmgtfy.com/?q={term}", description="Cant do anything more than this find your query by going on this link lazy idiot!")
        await ctx.send(link, embed=embed)

    @google.error
    async def google_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You have to send what you want to google with the command!")
     
    @commands.command()
    @commands.guild_only()
    async def clap(self,ctx,term):
        letters = len(term)
        if letters:
            for letter in term:
                await ctx.send(f"{letter}:clap:" )

    @commands.command()
    @commands.guild_only()
    async def simprate(self, ctx, member: discord.Member = None):
        simp = random.randrange(1,100)
        if member == None:
            await ctx.send(f"{ctx.author.name} is {simp}% simp")
        else:
            await ctx.send(f"{ctx.author.name} is {simp}% simp")
    @commands.command()
    @commands.guild_only()
    async def dankrate(self, ctx, member: discord.Member = None):
        dank = random.randrange(1,100)
        if member == None:
            await ctx.send(f"{ctx.author.name} is {dank}% dank")
        else:
            await ctx.send(f"{ctx.author.name} is {dank}% dank")
    @commands.command()
    @commands.guild_only()
    async def stankrate(self, ctx, member: discord.Member = None):
        stank = random.randrange(1,100)
        if member == None:
            await ctx.send(f"{ctx.author.name} is {stank}% stank")
        else:
            await ctx.send(f"{ctx.author.name} is {stank}% stank")
    @commands.command()
    @commands.guild_only()
    async def coolrate(self, ctx, member: discord.Member = None):
        cool = random.randrange(1,100)
        if member == None:
            await ctx.send(f"{ctx.author.name} is {cool}% cool")
        else:
            await ctx.send(f"{ctx.author.name} is {cool}% cool")
    @commands.command()
    @commands.guild_only()
    async def chumprate(self, ctx, member: discord.Member = None):
        chump = random.randrange(1,100)
        if member == None:
            await ctx.send(f"{ctx.author.name} is {chump}% chump")
        else:
            await ctx.send(f"{ctx.author.name} is {chump}% chump")
    @commands.command()
    @commands.guild_only()
    async def roast(self, ctx, member: discord.Member = None):
        roast = random.choice(["You are a pizza burn on the roof of the world's mouth","You losing your virginity is like a summer squash growing in the middle of winter. Never happening","You are dumber than a block of wood and not nearly as useful","You’re the reason God created the middle finger.","You’re a grey sprinkle on a rainbow cupcake.","If your brain was dynamite, there wouldn’t be enough to blow your hat off"," You are more disappointing than an unsalted pretzel.","Light travels faster than sound which is why you seemed bright until you spoke."," You have so many gaps in your teeth it looks like your tongue is in jail.","Your face makes onions cry.","Don’t be ashamed of who you are. That’s your parents’ job."])
        if member == None:
            await ctx.send(f"{roast}") 
        else:
            await ctx.send(f"{roast}") 
def setup(bot):
    bot.add_cog(Fun(bot))
    