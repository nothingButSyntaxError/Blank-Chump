import asyncio
import discord
import datetime
from discord import colour
from discord.ext import commands
import os
import pymongo
from pymongo import MongoClient
import random
from PIL import ImageFont, Image, ImageDraw
from io import BytesIO

guild_cluster = MongoClient("mongodb+srv://Yash:BlankChump@cluster0.qbjak.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
guild_db = guild_cluster["discord"]
collection = guild_db["server_data"]
def check(ctx):
    if ctx.author == ctx.guild.owner:
        return True
    else:
        return False
class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['guildinfo'])
    async def serverinfo(self, ctx):
        guild = ctx.message.guild
        stat_mem = len(guild.members)
        stat_roles = len(guild.roles)
        stat_creation = guild.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")
        safety_verification = guild.verification_level
        safety_content = guild.explicit_content_filter
        safety_2FA = guild.mfa_level
        stuff_owner = guild.owner
        stuff_region = discord.VoiceRegion
        embed = discord.Embed(title=guild.name, colour=ctx.author.colour)
        embed.add_field(name="Stats", value=f"**Members:** {stat_mem}\n**Roles:** {stat_roles}\n**Created At:** {stat_creation}")
        embed.add_field(name="Safety", value=f"**Verification Level:** {safety_verification}\n**Content Filter:** {safety_content}\n**2FA Level:** {safety_2FA}")
        embed.add_field(name="Stuff", value=f"**Owner:** {stuff_owner}\n**Region:** {stuff_region}")
        embed.set_thumbnail(url=guild.icon_url)
        embed.set_footer(text=f"{guild.id}")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.check(check)
    async def changeprefix(self, ctx, prefix:str = None):
        guild = ctx.guild
        guild_data = collection.find_one({"guild_id":guild.id})
        if not guild_data:
            collection.insert_one({"guild_id":guild.id, "prefix":"%"})  
            await ctx.send("Your guild was added") 
            return
        else :
            if prefix == None :
                await ctx.send("You have to mention the prefix you want to set along with the command")
            else: 
                collection.update_one({"guild_id":guild.id},{"$set":{"prefix":prefix}}) 
                await ctx.send(f"Prefix was changed to {prefix}")   

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        act_tim = datetime.datetime.utcnow()
        embed = discord.Embed(title="Thank You!", description=f"Thank you for adding {self.bot.user} to your server!", colour=discord.Colour.gold())
        embed.add_field(name="Setup Instructions", value=f"To setup the bot please do look at the `%help` command to add your guild to the bots data and so you can use its premium features as well!")
        embed.set_author(name=f"{guild.owner}")
        embed.set_footer(text=f"{act_tim}")
        embed.set_thumbnail(url=guild.owner.avatar_url)
        await guild.owner.send(embed=embed)
        guild_info = collection.find_one({"guild_id":guild.id})
        if not guild_info:
            collection.insert_one({"guild_id":guild.id,"prefix":"%"})
        else:
            pass 

    @commands.command(help = "Chooses 1 object when provided 2 or more objects", aliases = ["choices"])
    @commands.guild_only()
    async def choose(self, ctx, *choices):
        if choices :
            term = random.choice(choices)
            await ctx.send(term)
        else:
            await ctx.send("You have to give some options to choose from")

    @commands.command(help = "Makes a list for you", aliases = ["lm", "dataorganizer"])
    @commands.guild_only()
    async def listmaker(self, ctx, *choices):
        if choices :
            term = random.choice([choices])
            await ctx.send(term)
        else:
            await ctx.send("Please provide objects for the list")
    

    @commands.command()
    @commands.guild_only()
    async def removemydata(self, ctx):
        await ctx.send("If you respond with yes, all your data including your currency data will be deleted from our database. If you want to continue with this, message yes, else message no. You have 30 seconds to answer")
        def check (m):
            return m.channel == ctx.channel
        msg = await self.bot.wait_for("message", check=check, timeout=30)
        if msg.content == "yes":
            await ctx.send("Your data is getting deleted now")
        elif msg.content == "no":
            await ctx.send("Your data will not get deleted")

    
    
      
    @commands.command(aliases=["whois"])
    async def userinfo(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author 
        else:
            roles = [role for role in member.roles]
            embed = discord.Embed(colour=discord.Colour.blue(), timestamp=ctx.message.created_at,title=f"User Info - {member}")
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text=f"Requested by {ctx.author}")
            embed.add_field(name="ID:", value=member.id)
            embed.add_field(name="Display Name:", value=member.display_name)
            embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
            embed.add_field(name="Joined Server On:", value=member.joined_at.strftime)
            embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
            embed.add_field(name="Highest Role:", value=member.top_role.mention)
            print(member.top_role.mention)
            await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"The ping I am currently recieving is **{round(self.bot.latency*1000)}ms**")


def setup(bot):
    bot.add_cog(Utility(bot))
