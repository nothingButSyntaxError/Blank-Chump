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
    async def roast(self, ctx, member: discord.Member = None):
        roast = random.choice(["You are a pizza burn on the roof of the world's mouth","You losing your virginity is like a summer squash growing in the middle of winter. Never happening","You are dumber than a block of wood and not nearly as useful","You’re the reason God created the middle finger.","You’re a grey sprinkle on a rainbow cupcake.","If your brain was dynamite, there wouldn’t be enough to blow your hat off"," You are more disappointing than an unsalted pretzel.","Light travels faster than sound which is why you seemed bright until you spoke."," You have so many gaps in your teeth it looks like your tongue is in jail.","Your face makes onions cry.","Don’t be ashamed of who you are. That’s your parents’ job."])
        if member == None:
            await ctx.send(f"{roast}") 
        else:
            await ctx.send(f"{roast}") 
    @commands.command()
    @commands.guild_only()
    async def _8ball(self, ctx, *, question):
        _8ball = random.choice(["Yes, ","No"])
        if question :
            await ctx.send(f"{_8ball}, you noob") 
        else:
            await ctx.send("Please state your question") 
    @commands.command()
    @commands.guild_only()
    async def  say(self, ctx, *, sentence):
        if sentence :
            await ctx.send(f"{sentence} \n\n -{ctx.author}")
        else:
            await ctx.send("Please type a sentence to be said")

    @commands.command()
    @commands.guild_only()
    async def simprate(self, ctx, member: discord.Member = None):
        simp = random.randrange(1,100)
        if member == None:
            embed = discord.Embed(title = f"Simp Rate machine \n\n {ctx.author.name} is {simp}% simp", colour = discord.Colour.dark_red())
            await ctx.send(embed = embed)
        else:
            await ctx.send(embed = embed)
    @commands.command()
    @commands.guild_only()
    async def dankrate(self, ctx, member: discord.Member = None):
        dank = random.randrange(1,100)
        if member == None:
           embed = discord.Embed(title = f"Dank Rate machine \n\n {ctx.author.name} is {dank}% dank", colour = discord.Colour.gold())
           await ctx.send(embed = embed)
        else:
            await ctx.send(embed = embed)
    @commands.command()
    @commands.guild_only()
    async def stankrate(self, ctx, member: discord.Member = None):
        stank = random.randrange(1,100)
        if member == None:
            embed = discord.Embed(title = f"Stank Rate machine \n\n {ctx.author.name} is {stank}% stank", colour = discord.Colour.teal())
            await ctx.send(embed = embed)
        else:
            await ctx.send(embed = embed)
    @commands.command()
    @commands.guild_only()
    async def coolrate(self, ctx, member: discord.Member = None):
        cool = random.randrange(1,100)
        if member == None:
            embed = discord.Embed(title = f"Cool Rate machine \n\n {ctx.author.name} is {cool}% cool", colour = discord.Colour.blue())
            await ctx.send(embed = embed)
        else:
            await ctx.send(embed = embed)
    @commands.command()
    @commands.guild_only()
    async def chumprate(self, ctx, member: discord.Member = None):
        chump = random.randrange(1,100)
        if member == None:
            embed = discord.Embed(title = f"Chump Rate machine \n\n {ctx.author.name} is {chump}% chump", colour = discord.Colour.green())
            await ctx.send(embed = embed)
        else:
            await ctx.send(embed = embed)
    @commands.command()
    @commands.guild_only()
    async def epicgamerrate(self, ctx, member: discord.Member = None):
        epicgamer = random.randrange(1,100)
        if member == None:
            embed = discord.Embed(title = f"Epic Gamer Rate machine :video_game: \n\n {member} is {epicgamer}% epic gamer", colour = discord.Colour.gold())
            await ctx.send(embed = embed)
        else:
            embed_1 = discord.Embed(title = f"Epic Gamer Rate machine :video_game: \n\n {ctx.author.name} is {epicgamer}% epic gamer", colour = discord.Colour.gold())
            await ctx.send(embed_1 = embed_1)
    @commands.command()
    @commands.guild_only()
    async def waifurate(self, ctx, member: discord.Member = None):
       waifu = random.randrange(1,100)
       if member :
            embed = discord.Embed(title = f"Waifu Rate machine \n\n {member} is {waifu}% waifu", colour = discord.Colour.dark_theme())
            await ctx.send(embed = embed)
       else:
            embed_1 = discord.Embed(title = f"Waifu Rate machine \n\n {ctx.author.name} is {waifu}% waifu", colour = discord.Colour.dark_theme())
            await ctx.send(embed_1 = embed_1)
    @commands.command()
    @commands.guild_only()
    async def howgay(self, ctx, member: discord.Member = None):
        gay = random.randrange(1,100)
        if member :
            embed = discord.Embed(title = f"Gay Rate machine :video_game: \n\n {member} is {gay}% gay", colour = discord.Colour.purple())
            await ctx.send(embed = embed)
        else:
            embed_1 = discord.Embed(title = f"Gay Rate machine :video_game: \n\n {ctx.author.name} is {gay}% gay", colour = discord.Colour.purple())
            await ctx.send(embed_1 = embed_1)

def setup(bot):
    bot.add_cog(Fun(bot))
    