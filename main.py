from cogs.images import Images
from cogs.games import games
from discord.ext.commands.core import check
from discord.flags import Intents
import pymongo
from pymongo import MongoClient
import discord
from discord.ext import commands
import os
import random
from pymongo import results
from discord.ext.commands.cooldowns import BucketType
import sqlite3

try:
    conn = sqlite3.connect('prefixes.sqlite')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS prefixes (
        guild INTEGER,
        prefix TEXT,
        owner TEXT
    );""")
    print("Prefixes are ready!")
except:
    print("Prefixes table, not created!")

guild_cluster = MongoClient("mongodb+srv://Parth:Blank-Chump@cluster0.qbjak.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
guild_cluster = MongoClient("mongodb+srv://Yash:BlankChump@cluster0.qbjak.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
guild_db = guild_cluster["discord"]
collection = guild_db["server_data"]

def get_prefix(self, ctx):
    guild_id = ctx.guild.id
    prefix = cur.execute("SELECT prefix FROM prefixes WHERE guild=?", (guild_id,)).fetchone()
    conn.commit()
    return prefix


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='%', intents=intents)

class MyHelp(commands.HelpCommand):
    def get_command_signature(self, command):
        return '%s%s%s' % (self.clean_prefix, command.qualified_name, command.signature)

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="Blank Chump Help", colour=discord.Colour.gold())
        for cog, commands in mapping.items():
            filtered = await self.filter_commands(commands, sort=True)
            cog_name = getattr(cog, "qualified_name", "No Category")
            embed.add_field(name=cog_name, value=f"`%help {cog_name}`", inline=True)

        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_cog_help(self, cog):
        embed = discord.Embed(title=cog.qualified_name,description="\n".join(self.get_command_signature(c) for c in cog.walk_commands()))

        channel = self.get_destination()
        await channel.send(embed=embed)


    async def send_command_help(self, command):
        embed = discord.Embed(title=self.get_command_signature(command), colour=discord.Colour.orange())
        embed.add_field(name="Description", value=command.help)
        alias = command.aliases
        usage = command.usage
        if alias:
            embed.add_field(name="Aliases", value=", ".join(alias), inline=False)
        if usage:
            embed.add_field(name="Usage", value=f"{usage}")

        channel = self.get_destination()
        await channel.send(embed=embed)


bot.help_command = MyHelp()


bot.load_extension(f"cogs.currency")
bot.load_extension(f"cogs.utility")
bot.load_extension(f"cogs.fun")
bot.load_extension(f"cogs.games")
bot.load_extension(f"cogs.images")
bot.load_extension(f"cogs.admin")
bot.load_extension(f"cogs.animals")


bot.run('ODA5NzM1NDgzNzEwMTExNzY0.YCZa7w.4qz1St9r9ktva6AANexlBNtEeeA')
