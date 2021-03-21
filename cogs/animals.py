from sqlite3.dbapi2 import connect
import discord
from discord import user
from discord import colour
from discord.ext import commands, tasks
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
        elif pet == 'mongoose':
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
        elif pet == 'heron':
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
        elif pet == 'parrot':
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
        elif pet == 'dog':
            if bank > 17999:
                a100 = 100
                a1 = 1
                await ctx.send("What do you want to name your dog? Please type the name out!")
                def dog_check(m):
                    return m.channel == ctx.channel
                msg = await self.bot.wait_for('message', check=dog_check)
                cursor.execute("INSERT INTO pets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (ctx.author.id, ctx.author.name, pet, msg.content, a100, a100, a100, a100, a1, a1))
                connection.commit()
                collection.update_one({"user": ctx.author.id}, {"$set": {"bank": bank-18000}})
                await ctx.send("You successfuly bought a dog for 18000 coins!")
            else:
                await ctx.send("You don't have enough money in your bank account to buy a dog!")
        elif pet == 'fox':
            if bank > 44999:
                a100 = 100
                a1 = 1
                await ctx.send("What do you want to name your foxxy? Please type the name out!")
                def fox_check(m):
                    return m.channel == ctx.channel
                msg = await self.bot.wait_for('message', check=fox_check)
                cursor.execute("INSERT INTO pets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (ctx.author.id, ctx.author.name, pet, msg.content, a100, a100, a100, a100, a1, a1))
                connection.commit()
                collection.update_one({"user": ctx.author.id}, {"$set": {"bank": bank-45000}})
                await ctx.send("You successfuly bought a fox for 45000 coins!")
            else:
                await ctx.send("You don't have enough money in your bank account to buy a fox")
        elif pet == 'wolf':
            if bank > 24999:
                a100 = 100
                a1 = 1
                await ctx.send("What do you want to name your wolf? Please type the name out!")
                def howl_check(m):
                    return m.channel == ctx.channel
                msg = await self.bot.wait_for('message', check=howl_check)
                cursor.execute("INSERT INTO pets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (ctx.author.id, ctx.author.name, pet, msg.content, a100, a100, a100, a100, a1, a1))
                connection.commit()
                collection.update_one({"user": ctx.author.id}, {"$set": {"bank": bank-25000}})
                await ctx.send("You successfuly bought a wolf for 25000 coins!")
            else:
                await ctx.send("You don't have enough money in your bank account to buy a wolf")
        elif pet == 'snake':
            if bank > 27999:
                a100 = 100
                a1 = 1
                await ctx.send("What do you want to name your pet snake? Please type the name out!")
                def cat_check(m):
                    return m.channel == ctx.channel
                msg = await self.bot.wait_for('message', check=cat_check)
                cursor.execute("INSERT INTO pets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (ctx.author.id, ctx.author.name, pet, msg.content, a100, a100, a100, a100, a1, a1))
                connection.commit()
                collection.update_one({"user": ctx.author.id}, {"$set": {"bank": bank-28000}})
                await ctx.send("You successfuly bought a snake for 28000 coins!")
            else:
                await ctx.send("You don't have enough money in your bank account to buy a snake.")
        elif pet == 'owl':
            if bank > 9999:
                a100 = 100
                a1 = 1
                await ctx.send("What do you want to name your owl? Please type the name out!")
                def cat_check(m):
                    return m.channel == ctx.channel
                msg = await self.bot.wait_for('message', check=cat_check)
                cursor.execute("INSERT INTO pets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (ctx.author.id, ctx.author.name, pet, msg.content, a100, a100, a100, a100, a1, a1))
                connection.commit()
                collection.update_one({"user": ctx.author.id}, {"$set": {"bank": bank-10000}})
                await ctx.send("You successfuly bought a owl for 10000 coins!")
            else:
                await ctx.send("You don't have enough money in your bank account to buy a owl")
        elif pet == 'eagle':
            if bank > 42999:
                a100 = 100
                a1 = 1
                await ctx.send("What do you want to name your pet eagle? Please type the name out!")
                def cat_check(m):
                    return m.channel == ctx.channel
                msg = await self.bot.wait_for('message', check=cat_check)
                cursor.execute("INSERT INTO pets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (ctx.author.id, ctx.author.name, pet, msg.content, a100, a100, a100, a100, a1, a1))
                connection.commit()
                collection.update_one({"user": ctx.author.id}, {"$set": {"bank": bank-43000}})
                await ctx.send("You successfuly bought a cat for 43000 coins!")
            else:
                await ctx.send("You don't have enough money in your bank account to buy a eagle!")
        else:
            await ctx.send("Hey there is no such thing in the pet list you idiot! Use the command petlist to see all the pets available!")
        

    @commands.command()
    async def petactions(self, ctx):
        pet_check = cursor.execute("SELECT * FROM pets WHERE id=?", (ctx.author.id,)).fetchone()
        if pet_check:
            embed = discord.Embed(title="Actions for your pet!", colour=discord.Colour.red())
            embed.add_field(name="%feedpet", value="Use the command to feed your pet!")
            embed.add_field(name="%petbath", value="Use the command for 50 coins to maintain hygiene for your pet!")
            embed.add_field(name="%trainpet", value="Use the command to train your pet in various fields!")
            embed.add_field(name="%pethunt", value="Use the command to go hunting with the pet!")
            embed.add_field(name="%disownpet", value="Use the command to disown your pet!")
            embed.add_field(name="%petplay", value="Use the command for playing with the pet!")
            embed.add_field(name="%petname", value="Use the command to change the pets name!")
            await ctx.send(embed=embed) 
        else:
            await ctx.send("You should own a pet for this!")

    @commands.command()
    async def petname(self, ctx, newname=None):
        petinfo = cursor.execute("SELECT * FROM pets WHERE id=?",(ctx.author.id,)).fetchone()
        if not petinfo:
            await ctx.send("Hey you should own a pet for chaning its name!")
        else:
            if newname == None:
                await ctx.send("**Your pets new name has to be sent along with the command**")
            elif newname != None:
                cursor.execute("UPDATE pets SET name=? WHERE id=?", (newname, ctx.author.id))
                await ctx.send(f"Your pet's name was changed to {newname}!")

    @tasks.loop(seconds=10)
    async def petloop(self):
        health = cursor.execute("SELECT health FROM pets").fetchall()
        for row in health:
            x = row[0]
        newhealth = x-1
        cursor.execute("UPDATE pets SET health=?", (newhealth,))

    @commands.command()
    async def feedpet(self, ctx):
        bankinfo = collection.find_one({"user":ctx.author.id})
        petinfo = cursor.execute("SELECT * FROM pets WHERE id=?", (ctx.author.id,)).fetchone()
        if not petinfo:
            await ctx.send("Hey you should own a pet for this. Consider buying one from the `%petlist` command!")
        else:
            etinfo = cursor.execute("SELECT name FROM pets WHERE id=?", (ctx.author.id,)).fetchone()
            expense = random.randrange(10, 30)
            wallet = bankinfo["wallet"]
            healthinfo = cursor.execute("SELECT health FROM pets WHERE id=?", (ctx.author.id,)).fetchone()
            newhealth = healthinfo + 1
            if expense > wallet:
                await ctx.send(f"You don't have enough money in your wallet to buy some food for {etinfo}! So sad!")
            else:
                await ctx.send(f"You bought food and water for {etinfo} and it cost you {expense} coins!")
                collection.update_one({"user":ctx.author.id}, {"$set":{"wallet":wallet-expense}})
                cursor.execute("UPDATE pets SET health=?", (newhealth,))
            






def setup(bot):
    bot.add_cog(Animals(bot))
