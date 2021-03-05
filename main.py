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

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='%', intents=intents)

bot.load_extension(f"cogs.functions")
bot.load_extension(f"cogs.currency")
bot.load_extension(f"cogs.utility")



bot.run('ODA5NzM1NDgzNzEwMTExNzY0.YCZa7w.4qz1St9r9ktva6AANexlBNtEeeA')
