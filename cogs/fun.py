import asyncio
import discord
from discord.ext import commands
import os
import random


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help = "Searches whatever you want on google", aliases = ["Search"])
    @commands.guild_only()
    async def google(self, ctx, term):
        link = f"http://lmgtfy.com/?q={term}"
        embed = discord.Embed(title="LMGTFY", url=f"https://lmgtfy.com/?q={term}", description="Cant do anything more than this find your query by going on this link lazy idiot!")
        await ctx.send(link, embed=embed)


    @google.error
    async def google_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You have to send what you want to google with the command!")

     
    @commands.command(help = "Types your word again with claps")
    @commands.guild_only()
    async def clap(self,ctx,term):
        letters = len(term)
        if letters:
            for letter in term:
                await ctx.send(f"{letter}:clap:" )
        else:
            await ctx.send("Type something to clap you dumbo:laughing:")   
                    

    @commands.command(help = "Doots all your words")
    @commands.guild_only()
    async def doot(self,ctx,term):
        letters = len(term)
        if letters:
            for letter in term:
                await ctx.send(f"{letter}💀🎺" )
        else:
            await ctx.send("Type something to doot you dumbo:laughing:")   


    @commands.command(help = "Roasts the person you mention", aliases = ["insult"])
    @commands.guild_only()
    async def roast(self, ctx, member: discord.Member = None):
        roast = random.choice(["You are a pizza burn on the roof of the world's mouth","You losing your virginity is like a summer squash growing in the middle of winter. Never happening","You are dumber than a block of wood and not nearly as useful","You’re the reason God created the middle finger.","You’re a grey sprinkle on a rainbow cupcake.","If your brain was dynamite, there wouldn’t be enough to blow your hat off"," You are more disappointing than an unsalted pretzel.","Light travels faster than sound which is why you seemed bright until you spoke."," You have so many gaps in your teeth it looks like your tongue is in jail.","Your face makes onions cry.","Don’t be ashamed of who you are. That’s your parents’ job."])
        if member == None:
            await ctx.send(f"{roast}") 
        else:
            await ctx.send(f"{roast}") 


    @commands.command(help = "Answers all your questions with either a yes or a no")
    @commands.guild_only()
    async def _8ball(self, ctx, *, question):
        _8ball = random.choice(["Yes, you noob ","No, I guess"])
        if question :
            await ctx.send(f":8ball: {_8ball}") 
        else:
            await ctx.send("Please state your question") 


    @commands.command(help = "Repeats everything that you say", aliases = ["print"])
    @commands.guild_only()
    async def  say(self, ctx, *, sentence):
        if sentence :
            await ctx.send(f"{sentence} \n\n -{ctx.author}")
        else:
            await ctx.send("Please type a sentence to be said")


    @commands.command(help = "Rates how simp you are", aliases=["simpr8"])
    @commands.guild_only()
    async def simprate(self, ctx, member: discord.Member = None):
        simp = random.randrange(1,100)
        if member :
            embed = discord.Embed(title = f"Simp Rate machine \n\n {member} is {simp}% simp", colour = discord.Colour.dark_red())
            await ctx.send(embed = embed)
        else:
            embed_1 = discord.Embed(title = f"Simp Rate machine \n\n {ctx.author.name} is {simp}% simp", colour = discord.Colour.dark_red())
            await ctx.send(embed = embed_1)


    @commands.command(help = "Rates how dank you are", aliases=["dankr8"])
    @commands.guild_only()
    async def dankrate(self, ctx, member: discord.Member = None):
        dank = random.randrange(1,100)
        if member:
           embed = discord.Embed(title = f"Dank Rate machine \n\n {member} is {dank}% dank", colour = discord.Colour.gold())
           await ctx.send(embed = embed)
        else:
            embed_1 = discord.Embed(title = f"Dank Rate machine \n\n {ctx.author.name} is {dank}% dank", colour = discord.Colour.gold())
            await ctx.send(embed = embed_1)


    @commands.command(help = "Rates how stank you are", aliases=["stankr8"])
    @commands.guild_only()
    async def stankrate(self, ctx, member: discord.Member = None):
        stank = random.randrange(1,100)
        if member == None:
            embed = discord.Embed(title = f"Stank Rate machine \n\n {member} is {stank}% stank", colour = discord.Colour.teal())
            await ctx.send(embed = embed)
        else:
            embed_1 = discord.Embed(title = f"Stank Rate machine \n\n {ctx.author.name} is {stank}% stank", colour = discord.Colour.teal())
            await ctx.send(embed = embed_1)


    @commands.command(help = "Rates how cool you are", aliases=["coolr8"])
    @commands.guild_only()
    async def coolrate(self, ctx, member: discord.Member = None):
        cool = random.randrange(1,100)
        if member :
            embed = discord.Embed(title = f"Cool Rate machine \n\n {member} is {cool}% cool", colour = discord.Colour.blue())
            await ctx.send(embed = embed)
        else:
            embed_1 = discord.Embed(title = f"Cool Rate machine \n\n {ctx.author.name} is {cool}% cool", colour = discord.Colour.blue())
            await ctx.send(embed = embed_1)


    @commands.command(help = "Rates how chump you are", aliases=["chumpr8"])
    @commands.guild_only()
    async def chumprate(self, ctx, member: discord.Member = None):
        chump = random.randrange(1,100)
        if member :
            embed = discord.Embed(title = f"Chump Rate machine \n\n {member} is {chump}% chump", colour = discord.Colour.green())
            await ctx.send(embed = embed)
        else:
            embed_1 = discord.Embed(title = f"Chump Rate machine \n\n {ctx.author.name} is {chump}% chump", colour = discord.Colour.green())
            await ctx.send(embed = embed_1)


    @commands.command(help = "Rates how epic you are as a gamer", aliases=["egr8"])
    @commands.guild_only()
    async def epicgamerrate(self, ctx, member: discord.Member = None):
        epicgamer = random.randrange(1,100)
        if member :
            embed = discord.Embed(title = f"Epic Gamer Rate machine :video_game: \n\n {member} is {epicgamer}% epic gamer", colour = discord.Colour.gold())
            await ctx.send(embed = embed)
        else:
            embed_1 = discord.Embed(title = f"Epic Gamer Rate machine :video_game: \n\n {ctx.author.name} is {epicgamer}% epic gamer", colour = discord.Colour.gold())
            await ctx.send(embed = embed_1)


    @commands.command(help = "Rates how waifu you are", aliases=["waifur8"])
    @commands.guild_only()
    async def waifurate(self, ctx, member: discord.Member = None):
       waifu = random.randrange(1,100)
       if member :
            embed = discord.Embed(title = f"Waifu Rate machine \n\n {member} is {waifu}% waifu", colour = discord.Colour.dark_magenta())
            await ctx.send(embed = embed)
       else:
            embed_1 = discord.Embed(title = f"Waifu Rate machine \n\n {ctx.author.name} is {waifu}% waifu", colour = discord.Colour.dark_magenta())
            await ctx.send(embed = embed_1)


    @commands.command(help = "Rates how gay you are", aliases=["gayr8", "gayrate"])
    @commands.guild_only()
    async def howgay(self, ctx, member: discord.Member = None):
        gay = random.randrange(1,100)
        if member :
            embed = discord.Embed(title = f"Gay Rate machine \n\n {member} is {gay}% gay", colour = discord.Colour.purple())
            await ctx.send(embed = embed)
        else:
            embed_1 = discord.Embed(title = f"Gay Rate machine \n\n {ctx.author.name} is {gay}% gay", colour = discord.Colour.purple())
            await ctx.send(embed = embed_1)
    

    @commands.command(help = "Ranks how thoughtful you are", aliases = ["thotr8", "thotrate",])
    @commands.guild_only()
    async def rankthot(self, ctx, member: discord.Member = None ):
        thot = random.randrange(1,100)
        if member :
            embed = discord.Embed(title = f"Thought Rate machine \n\n {member} is {thot}% thoughtful", colour = discord.Colour.purple())
            await ctx.send(embed = embed)
        else:
            embed_1 = discord.Embed(title = f"Thought Rate machine \n\n {ctx.author.name} is {thot}% thoughtful", colour = discord.Colour.purple())
            await ctx.send(embed = embed_1)


    @commands.command(help = "Hacks the person who you mention", aliases = ["datarob"])
    @commands.guild_only()
    async def hack(self, ctx, member: discord.Member = None):
        if member == None:
            await ctx.send("You need to name someone to hack!!!")
        else: 
            msg = await ctx.send(f"Hacking {member.name} now")
            await asyncio.sleep(2)
            await msg.edit(content = "Adding all information to database" )
            await asyncio.sleep(2)
            await msg.edit(content = "Sending data to government")
            await asyncio.sleep(2)
            await msg.edit(content = "Sending all data secrets to you")
            await asyncio.sleep(2)
            await msg.edit(content = "Loading virus in the software...")
            await asyncio.sleep(2)
            await msg.edit(content = "Spreading data around the internet to see")
            await asyncio.sleep(2)
            await msg.edit(content = "The totally real and actually existing hack is complete.")
    

    @commands.command(help = "Redacts any message you send", aliases = ["redactor"] )
    @commands.guild_only()
    async def spoiler(self, ctx, *, redacteds = None):
        if redacteds == None :
             await ctx.send("You need to send some words to be redacted")
        else :
            for redacted in redacteds :
                blackwords= (f"||{redacted}||")
            await ctx.send(blackwords)

    
    @commands.command(help = "It says OwO", aliases = ["OwO"])
    @commands.guild_only()
    async def owo(self, ctx):
        await ctx.send("OwO")

    @commands.command(help = "Vaporwaves your words. Try it out")
    @commands.guild_only()
    async def vaporwave(self,ctx, *, term = None):
        if term!= None:
            for letter in term:
                await ctx.send(f"{letter} " )
        elif term == None:
            await ctx.send("Type something to vaporwave you dumbo:laughing:")  


    @commands.command(help = "Rickrolls any member of discord on your behalf. This command works in the BlankChump private chat also", aliases = ["astley", "prank"])  
    async def rickroll(self, ctx, member: discord.Member = None):
        if member != None:
            
            try:
                msg = await member.send(f"{ctx.author.name} has sent this special link for you \n https://youtu.be/dQw4w9WgXcQ")
                await msg.edit(suppress = True )
                await ctx.message.delete()
            except:
                await ctx.send("The member is not accepting DM's")
        else:
            await ctx.send("You have to mention a member to rickroll, or I will rickroll you :smiley: ")
    

    


    

    

           

    


def setup(bot):
    bot.add_cog(Fun(bot))
    