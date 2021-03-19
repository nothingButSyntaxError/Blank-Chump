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
import pymongo
from pymongo import MongoClient

#MONGODB
cluster = MongoClient("mongodb+srv://Admin-MyName:Parth!7730@my-dbs.xlx4y.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["discord"]
collection = db["user_data"]

#SQLITE
try:
    connection = sqlite3.connect("./pets.sqlite")
    cursor = connection.cursor()
    print("Connection successful!")
except Error:
    print(Error)

pets = [{"name":"cat", "price":8000},
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
        bankinfo = collection.find_one({"user":ctx.author.id})
        wallet = bankinfo["wallet"]
        bank = bankinfo["bank"]
        cursor.execute("""CREATE TABLE IF NOT EXISTS pets (
            id INTEGER,
            user_name TEXT,
            pet_type TEXT,
            name TEXT,
            health INTEGER,
            love INTEGER,
            hunger INTEGER,
            fun INTEGER,
            experince INTEGER,
            level INTEGER
        );""")
        connection.commit()
        if pet == 'cat':
            if bank > 7999:
                a100 = 100
                a1 = 1
                await ctx.send("What do you want to name your cat? Please type the name out!")
                def cat_check(m):
                    return m.channel == ctx.channel
                msg = await self.bot.wait_for('message', check=cat_check)
                cursor.execute("INSERT INTO pets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(ctx.author.id, ctx.author.name, pet, msg.content, a100, a100, a100, a100, a1, a1))
                connection.commit()
                collection.update_one({"user":ctx.author.id}, {"$set":{"bank":bank-8000}})
                await ctx.send("You successfuly bought a cat for 8000 coins!")
            else:
                await ctx.send("You don't have enough money in your bank account to buy a cat")
        if pet == 'mongoose':
            if bank > 39999:
                a100 = 100
                a1 = 1
                await ctx.send("What do you want to name your mongoose? Please type the name out!")
                def mong_check(m):
                    return m.channel == ctx.channel
                msg = await self.bot.wait_for('message', check=mong_check)
                cursor.execute("INSERT INTO pets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (ctx.author.id, ctx.author.name, pet, msg.content, a100, a100, a100, a100, a1, a1))
                connection.commit()
                collection.update_one({"user": ctx.author.id}, {"$set": {"bank": bank-40000}})
                await ctx.send("You successfuly bought a mongoose for 40000 coins!")
            else:
                await ctx.send("You don't have enough money in your bank account to buy a mongoose")
        if pet == 'heron':
            if bank > 29999:
                a100 = 100
                a1 = 1
                await ctx.send("What do you want to name your heron? Please type the name out!")
                def hero_check(m):
                    return m.channel == ctx.channel
                msg = await self.bot.wait_for('message', check=hero_check)
                cursor.execute("INSERT INTO pets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (ctx.author.id, ctx.author.name, pet, msg.content, a100, a100, a100, a100, a1, a1))
                connection.commit()
                collection.update_one({"user": ctx.author.id}, {"$set": {"bank": bank-30000}})
                await ctx.send("You successfuly bought a heron for 30000 coins!")
            else:
                await ctx.send("You don't have enough money in your bank account to buy a heron")
        if pet == 'parrot':
            if bank > 14999:
                a100 = 100
                a1 = 1
                await ctx.send("What do you want to name your parrot? Please type the name out!")
                def parrot_check(m):
                    return m.channel == ctx.channel
                msg = await self.bot.wait_for('message', check=parrot_check)
                cursor.execute("INSERT INTO pets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (ctx.author.id, ctx.author.name, pet, msg.content, a100, a100, a100, a100, a1, a1))
                connection.commit()
                collection.update_one({"user": ctx.author.id}, {"$set": {"bank": bank-15000}})
                await ctx.send("You successfuly bought a cat for 15000 coins!")
            else:
                await ctx.send("You don't have enough money in your bank account to buy a parrot")
        #if pet == '':
         #   if bank > 7999:
          #      a100 = 100
           #     a1 = 1
            #    await ctx.send("What do you want to name your cat? Please type the name out!")
             #   def cat_check(m):
              #      return m.channel == ctx.channel
               # msg = await self.bot.wait_for('message', check=cat_check)
                #cursor.execute("INSERT INTO pets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                 #   ctx.author.id, ctx.author.name, pet, msg.content, a100, a100, a100, a100, a1, a1))
               # connection.commit()
                #collection.update_one({"user": ctx.author.id}, {
                 #                     "$set": {"bank": bank-8000}})
               # await ctx.send("You successfuly bought a cat for 8000 coins!")
            #else:
             #   await ctx.send("You don't have enough money in your bank account to buy a cat")
        #if pet == 'cat':
         #   if bank > 7999:
          #      a100 = 100
           #     a1 = 1
            #    await ctx.send("What do you want to name your cat? Please type the name out!")
              #  def cat_check(m):
               #     return m.channel == ctx.channel
                #msg = await self.bot.wait_for('message', check=cat_check)
                #cursor.execute("INSERT INTO pets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                #    ctx.author.id, ctx.author.name, pet, msg.content, a100, a100, a100, a100, a1, a1))
                #connection.commit()
                #collection.update_one({"user": ctx.author.id}, {
                 #                     "$set": {"bank": bank-8000}})
                #await ctx.send("You successfuly bought a cat for 8000 coins!")
            #else:
             #   await ctx.send("You don't have enough money in your bank account to buy a cat")
        #if pet == 'cat':
         #   if bank > 7999:
          #      a100 = 100
           #     a1 = 1
            #    await ctx.send("What do you want to name your cat? Please type the name out!")
#
 #               def cat_check(m):
  #                  return m.channel == ctx.channel
   #             msg = await self.bot.wait_for('message', check=cat_check)
    #            cursor.execute("INSERT INTO pets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
     #               ctx.author.id, ctx.author.name, pet, msg.content, a100, a100, a100, a100, a1, a1))
      #          connection.commit()
       #         collection.update_one({"user": ctx.author.id}, {
        #                              "$set": {"bank": bank-8000}})
         #       await ctx.send("You successfuly bought a cat for 8000 coins!")
          #  else:
           #     await ctx.send("You don't have enough money in your bank account to buy a cat")
        #if pet == 'cat':
         #   if bank > 7999:
          #      a100 = 100
           #     a1 = 1
            #    await ctx.send("What do you want to name your cat? Please type the name out!")
             #   def cat_check(m):
              #      return m.channel == ctx.channel
               # msg = await self.bot.wait_for('message', check=cat_check)
                #cursor.execute("INSERT INTO pets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                 #   ctx.author.id, ctx.author.name, pet, msg.content, a100, a100, a100, a100, a1, a1))
                #connection.commit()
                #collection.update_one({"user": ctx.author.id}, {
                #                      "$set": {"bank": bank-8000}})
                #await ctx.send("You successfuly bought a cat for 8000 coins!")
            #else:
             #   await ctx.send("You don't have enough money in your bank account to buy a cat")
        #if pet == 'cat':
         #   if bank > 7999:
          #      a100 = 100
           #     a1 = 1
            #    await ctx.send("What do you want to name your cat? Please type the name out!")
              #  def cat_check(m):
               #     return m.channel == ctx.channel
                #msg = await self.bot.wait_for('message', check=cat_check)
                #cursor.execute("INSERT INTO pets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                 #   ctx.author.id, ctx.author.name, pet, msg.content, a100, a100, a100, a100, a1, a1))
                #connection.commit()
         #       collection.update_one({"user": ctx.author.id}, {
          
          #                            "$set": {"bank": bank-8000}})
           #     await ctx.send("You successfuly bought a cat for 8000 coins!")
            #else:
             #   await ctx.send("You don't have enough money in your bank account to buy a cat")
       # if pet == 'cat':
         #   if bank > 7999:
        #        a100 = 100
          #      a1 = 1
           #     await ctx.send("What do you want to name your cat? Please type the name out!")
                #def cat_check(m):
                 #   return m.channel == ctx.channel
                #msg = await self.bot.wait_for('message', check=cat_check)
                #cursor.execute("INSERT INTO pets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                 #   ctx.author.id, ctx.author.name, pet, msg.content, a100, a100, a100, a100, a1, a1))
               # connection.commit()
                #collection.update_one({"user": ctx.author.id}, {
                 #                     "$set": {"bank": bank-8000}})
                #await ctx.send("You successfuly bought a cat for 8000 coins!")
            #else:
             #   await ctx.send("You don't have enough money in your bank account to buy a cat")
        





def setup(bot):
    bot.add_cog(Animals(bot))
