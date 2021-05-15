from typing import ValuesView
import discord
from discord import user
from discord import colour
from discord.ext import commands
import random
import os
import datetime

def bot_check(ctx):
    if ctx.author.bot == True:
        return False
    else:
        return True

class games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.check(bot_check)
    async def rps(self, ctx, mem_choice):
        bot_choice = random.choice(['rock', 'paper', 'scizzor'])
        if mem_choice == 'ROCK'.lower():
            if bot_choice == 'rock':
                embed = discord.Embed(title=f"{ctx.author.name}'s Tied RPS Game!", colour=discord.Colour.gold())
                embed.add_field(name="Bot Played:", value="rock")
                embed.add_field(name=f"{ctx.author.name} Played:", value="rock")
                embed.set_thumbnail(url=ctx.author.avatar_url)
                embed.set_footer(text=f"{datetime.datetime.utcnow()} UTC")
                await ctx.send(embed=embed)
            elif bot_choice == 'paper':
                em = discord.Embed(title=f"{ctx.author.name}'s Losing RPS Game!", colour=discord.Colour.red())
                em.add_field(name="Bot Played:", value="paper")
                em.add_field(name=f"{ctx.author.name} Played:", value="rock")
                em.set_thumbnail(url=ctx.author.avatar_url)
                em.set_footer(text=f"{datetime.datetime.utcnow()} UTC")
                await ctx.send(embed=em)
            elif bot_choice == 'scizzor':
                e = discord.Embed(title=f"{ctx.author.name}'s Winning RPS Game!", colour=discord.Colour.green())
                e.add_field(name="Bot Played:", value="scizzor")
                e.add_field(name=f"{ctx.author.name} Played:", value="rock")
                e.set_thumbnail(url=ctx.author.avatar_url)
                e.set_footer(text=f"{datetime.datetime.utcnow()} UTC")
                await ctx.send(embed=e)
        elif mem_choice == 'paper':
            if bot_choice == 'rock':
                em = discord.Embed(title=f"{ctx.author.name}'s Winning RPS Game!", colour=discord.Colour.green())
                em.add_field(name="Bot Played:", value="rock")
                em.add_field(name=f"{ctx.author.name} Played:", value="paper")
                em.set_thumbnail(url=ctx.author.avatar_url)
                em.set_footer(text=f"{datetime.datetime.utcnow()} UTC")
                await ctx.send(embed=em)
            elif bot_choice == 'paper':
                embed = discord.Embed(title=f"{ctx.author.name}'s Tied RPS Game!", colour=discord.Colour.gold())
                embed.add_field(name="Bot Played:", value="paper")
                embed.add_field(name=f"{ctx.author.name} Played:", value="paper")
                embed.set_thumbnail(url=ctx.author.avatar_url)
                embed.set_footer(text=f"{datetime.datetime.utcnow()} UTC")
                await ctx.send(embed=embed)
            elif bot_choice == 'scizzor':
                em = discord.Embed(title=f"{ctx.author.name}'s Losing RPS Game!", colour=discord.Colour.red())
                em.add_field(name="Bot Played", value="scizzor")
                em.add_field(name=f"{ctx.author.name} Played", value="paper")
                em.set_thumbnail(url=ctx.author.avatar_url)
                em.set_footer(text=f"{datetime.datetime.utcnow()} UTC")
                await ctx.send(embed=em)
        elif mem_choice == 'scizzor':
            if bot_choice == 'rock':
                em = discord.Embed(title=f"{ctx.author.name}'s Losing RPS Game!", colour=discord.Colour.red())
                em.add_field(name="Bot Played", value="rock")
                em.add_field(name=f"{ctx.author.name} Played", value="scizzor")
                em.set_footer(text=f"{datetime.datetime.utcnow()} UTC")
                em.set_thumbnail(url=ctx.author.avatar_url)
                await ctx.send(embed=em)
            elif bot_choice == 'paper':
                em = discord.Embed(title=f"{ctx.author.name}'s Winning RPS Game!", colour=discord.Colour.green())
                em.add_field(name="Bot Played", value="paper")
                em.add_field(name=f"{ctx.author.name} Played", value="scizzor")
                em.set_footer(text=f"{datetime.datetime.utcnow()} UTC")
                em.set_thumbnail(url=ctx.author.avatar_url)
                await ctx.send(embed=em)
            elif bot_choice == 'scizzor':
                em = discord.Embed(title=f"{ctx.author.name}'s Tied RPS Game!", colour=discord.Colour.gold())
                em.add_field(name="Bot Played", value="scizzor")
                em.add_field(name=f"{ctx.author.name} Played", value="scizzor")
                em.set_footer(text=f"{datetime.datetime.utcnow()} UTC")
                em.set_thumbnail(url=ctx.author.avatar_url)
                await ctx.send(embed=em)

    #@commands.command()
    @commands.check(bot_check)
    async def fight(self, ctx, member: discord.Member = None):
        if member == None:
            await ctx.send("You have to mention someone to fight them!!")
        elif member != None:
            if member.bot == True:
                await ctx.reply("The mentioned person cannot be a bot. Idiot!!!")
            else:
                player1 = ctx.author
                player2 = member
                await ctx.send(f"{player2.mention}, do you want to fight {player1.name}, if you accept the fight type the message `yes` below in the chat within 30 seconds!")
                def confirmcheck(m):
                    return m.author == player2 and m.channel == ctx.channel
                msg = await self.bot.wait_for('message', check=confirmcheck, timeout=30)
                if asyncio.TimeoutError:
                    await ctx.send("The fight challenge timed out!")
                elif msg.content == 'yes':
                    player1Health = 100
                    player2Health = 100
                    for player1Health == 0 or player2Health == 0:
                        await ctx.send(f"So what do you wanna do {player1.mention}, you can **punch**, **kick**, **defend**, **run away**")
                        def check(m):
                            return m.author == player1
                        message = await self.bot.wait_for('message', check=check, timeout=15)
                        if message.content == 'kick' or message.content == 'punch':
                            damage = random.randrange(5, 27)
                            await ctx.send(f"{player1.mention} landed a {message.content} on {player2} and dealt {damage} damage!")
                            player2Health = player2Health - damage
                        elif message.content == 'defend':
                            await ctx.send(f"{player1.mention} defended and increased his health by 10!")
                            player1Health = player1Health + 10
                            await ctx.send(f"So what do you wanna do {player2.mention}, you can **punch**, **kick**, **defend**, **run away**")


                



def setup(bot):
    bot.add_cog(games(bot))
