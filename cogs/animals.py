from sqlite3.dbapi2 import connect
import discord
from discord import user
from discord import colour
from discord.ext import commands
import random
import os
import praw
import sqlite3
from sqlite3 import Error

try:
    connection = sqlite3.connect("./pets.sqlite")
    cursor = connection.cursor()
    print("Connection successful!")
except Error:
    print(Error)

pets = [{"name":"cat", "price":5000},
        {"name":"mongoose", "price":40000},
        {"name":"heron", "price":30000},
        {"name":"parrot", "price":15000},
        {"name":"dog", "price":18000},
        {"name":"fox", "price":45000},
        {"name":"wolf", "price":25000},
        {"name":"snake", "price":28000},
        {"name":"owl", "price":10000},
        {"name":"eagle", "price":43000}]

class Animals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        

    @commands.command()
    async def petlist(self, ctx):
        embed = discord.Embed(title=f"{self.bot.user}'s Pet Shop!", colour=discord.Colour.blue())
        for item in pets:
            name = item["name"]
            price = item["price"]
            embed.add_field(name=f'**{name}**', value=f"{price}", inline=False)
            embed.set_footer(text="To buy something use %buypet 'pet'")
        await ctx.send(embed=embed)

        
    @commands.command()
    async def buypet(self, ctx, pet, amount=1):
        cursor.execute("""CREATE TABLE IF NOT EXISTS pets (
            id INTEGER,
            user_name TEXT,
            name TEXT,
            health INTEGER,
            love INTEGER,
            hunger INTEGER,
            fun INTEGER,
            experince INTEGER,
            level INTEGER
        );""")




def setup(bot):
    bot.add_cog(Animals(bot))
