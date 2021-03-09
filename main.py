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

guild_cluster = MongoClient("mongodb+srv://Yash:BlankChump@cluster0.qbjak.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
guild_db = guild_cluster["discord"]
collection = guild_db["server_data"]

def get_prefix(self, ctx):
    guild = ctx.guild
    guild_data = collection.find_one({"guild_id":guild.id})
    guild_prefix = guild_data["prefix"]
    return guild_prefix

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=get_prefix, intents=intents)


bot.load_extension(f"cogs.functions")
bot.load_extension(f"cogs.currency")
bot.load_extension(f"cogs.utility")
bot.load_extension(f"cogs.fun")


bot.run('ODA5NzM1NDgzNzEwMTExNzY0.YCZa7w.4qz1St9r9ktva6AANexlBNtEeeA')
