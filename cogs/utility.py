import asyncio
import discord
from discord import colour
from discord.ext import commands
import os
import pymongo
from pymongo import MongoClient

main_cluster = MongoClient('mongodb+srv://Admin-MyName:Parth!7730@my-dbs.xlx4y.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
main_db = main_cluster["discord"]
main_collection = main_db["guild_data"]

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

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




def setup(bot):
    bot.add_cog(Utility(bot))
