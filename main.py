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


class MyHelp(commands.HelpCommand):
    def get_command_signature(self, command):
        return '%s%s %s' % (self.clean_prefix, command.qualified_name, command.signature)

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="Help", colour=discord.Colour.dark_blue())
        for cog, commands in mapping.items():
           filtered = await self.filter_commands(commands, sort=True)
           command_signatures = [
               self.get_command_signature(c) for c in filtered]
           if command_signatures:
               cog_name = getattr(cog, "qualified_name", "No Category")
               embed.add_field(name=cog_name, value="\n".join(command_signatures), inline=False)

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


bot.load_extension(f"cogs.functions")
bot.load_extension(f"cogs.currency")
bot.load_extension(f"cogs.utility")
bot.load_extension(f"cogs.fun")


bot.run('ODA5NzM1NDgzNzEwMTExNzY0.YCZa7w.4qz1St9r9ktva6AANexlBNtEeeA')
