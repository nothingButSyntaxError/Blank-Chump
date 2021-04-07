from typing import Text
import discord
from discord.ext import commands, tasks
import os
import sqlite3

try:
    conn = sqlite3.connect("pokemons.sqlite")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS pokemons (
        user_id INTEGER,
        pokemon TEXT
    );""")
except:
    print("error while poke!")

class pokemon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pokestart(self, ctx):
        embed = discord.Embed(title="Choose from below which pokemon do you want to start your journey with using `%choose (your pokemon)` command!")
        embed.add_field(name="Kanto Region", value="Bulbasaur -- Charmander -- Squirtle", inline=False)
        embed.add_field(name="Johto Region", value="Chikorita -- Cyndaquil -- Totodile", inline=False)
        embed.add_field(name="Hoenn Region", value="Treecko -- Torchic -- Mudkip", inline=False)
        embed.add_field(name="Sinnoh Region", value="Turtwig -- Chimchar -- Piplup", inline=False)
        embed.add_field(name="Unova Region", value="Snivy -- Tepig -- Oshawott", inline=False)
        embed.add_field(name="Kalos Region", value="Chespin -- Fennekin -- Froakie", inline=False)
        embed.add_field(name="Alola Region", value="Rowlet -- Litten -- Popplio", inline=False)
        await ctx.send(embed=embed)

        



def setup(bot):
    bot.add_cog(pokemon(bot))