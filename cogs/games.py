from typing import ValuesView
import discord
from discord import user
from discord import colour
from discord.ext import commands
import random
import os
import datetime

#TICTACTOE

player1 = ""
player2 = ""
turn = ""
gameover = True

board = []
winningconditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

class games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
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
                em = discord.Embed(title=f"{ctx.author.name}'s Winning RPS Game!", colour=discord.Colour.green())
                em.add_field(name="Bot Played:", value="paper")
                em.add_field(name=f"{ctx.author.name} Played:", value="rock")
                em.set_thumbnail(url=ctx.author.avatar_url)
                em.set_footer(text=f"{datetime.datetime.utcnow()} UTC")
                await ctx.send(embed=em)
            elif bot_choice == 'scizzor':
                e = discord.Embed(title=f"{ctx.author.name}'s Losing RPS Game!", colour=discord.Colour.red())
                e.add_field(name="Bot Played:", value="scizzor")
                e.add_field(name=f"{ctx.author.name} Played:", value="rock")
                e.set_thumbnail(url=ctx.author.avatar_url)
                e.set_footer(text=f"{datetime.datetime.utcnow()} UTC")
                await ctx.send(embed=e)
        elif mem_choice == 'paper':
            if bot_choice == 'rock':
                em = discord.Embed(title=f"{ctx.author.name}'s Losing RPS Game!", colour=discord.Colour.red())
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

    
    @commands.command()
    @commands.guild_only()
    async def tictactoe(self, ctx, member1: discord.Member, member2: discord.Member):
        global player1
        global player2
        global turn
        global gameover
        global count

        if gameover:
            global board
            board = [":white_large_square:",":white_large_square:",":white_large_square:",
                     ":white_large_square:",":white_large_square:",":white_large_square:",
                     ":white_large_square:",":white_large_square:",":white_large_square:"]
            turn = ""
            gameover=False
            count=0
            player1=member1
            player2=member2

            line=""
            for x in range(len(board)):
                if x == 2 or x==5 or x==8:
                    line += " " +board[x]
                    await ctx.send(line)
                    line=""
                else:
                    line += " " +board[x]

            choice = random.randint(1,2)
            if choice == 1:
                turn == player1
                await ctx.send(f"It is <@{player1.id}>'s turn.")
            elif choice == 2:
                turn == player2
                await ctx.send(f"It is <@{player2.id}>'s turn.")

        else:
            await ctx.send("A game is already in progress. Finish it before starting a new one")
    
    @commands.command()
    @commands.guild_only()
    async def place(self, ctx, pos : int):
        global turn 
        global player1
        global player2
        global board
        global count
        
        if not gameover:
            mark = ""
            if turn == ctx.author:
                if turn == player1:
                    mark = ":regional_indicator_x"
                elif turn == player2:
                    mark = ":o2:"
                if 0<pos<10 and board[pos - 1] == ":white_large_square:":
                    board[pos - 1] = mark
                    count += 1

                    line=""
                    for x in range(len(board)):
                        if x == 2 or x==5 or x==8:
                            line += " " +board[x]
                            await ctx.send(line)
                            line=""
                        else:
                            line += " " +board[x]
                    if gameover:
                        await ctx.send(f"{mark} wins!")
                    elif count >= 9:
                        await ctx.send("It's a tie :laughing:")

                    if turn == player1:
                        turn == player2
                    elif turn == player2:
                        turn == player1
                else:
                    await ctx.send("Please use an integer between 1 and 9 and an unmarked square")
            else:
                await ctx.send("It is not your turn")
        else:
            await ctx.send("Please start a new game using the %tictactoe command.")

    def checkwinner(self, winningconditions, mark):
        global gameover
        for condition in winningconditions:
            if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
                gameover = True

    @tictactoe.error
    async def tictactoe_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please mention 2 players to play the game and make sure it is not a bot or a person who is offline.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Please mention the person you want to play with (i.e. <@809735483710111764")
    @place.error
    async def place_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please enter a position you would like to mark.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Please make sure to enter an integer")




def setup(bot):
    bot.add_cog(games(bot))
