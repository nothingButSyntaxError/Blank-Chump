import discord
from discord.ext import commands
import os

from discord.ext.commands.errors import MissingPermissions


bad_words = ['fuck', 'bitch', 'ass']

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message):
        for word in bad_words:
            if word in message.content:
                await message.delete()
                await message.channel.send("Don't send bad words please!")
                await message.author.send(f"You have been warned for sending bad words in {message.guild.name}. **Please dont do this again!**")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, reason=None):
        if member == None:
            await ctx.send("You can't really kick nobody right? Mention someone to kick them please!")
        elif member != None:
            await member.kick(reason=reason)
            await ctx.send(f"{member} was kicked by {ctx.author} for reason - {reason}")
            await member.send(f"Hey you were kicked from {ctx.guild.name} by {ctx.author} for reason - {reason}")

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You don't have that permission")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, reason=None):
        if member == None:
            await ctx.send("I cant really ban nobody right?? Mention someone to ban them please!")
        elif member != None:
            await member.ban(reason=reason)
            await ctx.send(f"{member} was banned by {ctx.author} for reason - {reason}")

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You don't have that permission")



def setup(bot):
    bot.add_cog(Moderation(bot))
