from sqlite3.dbapi2 import connect
from typing import ValuesView
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
from discord.ext.commands.cooldowns import BucketType


#MONGODB
<<<<<<< HEAD
self.cluster = MongoClient("mongodb+srv://Admin-MyName:<Passsword>@my-dbs.xlx4y.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
self.db = cluster["discord"]
self.collection = db["user_data"]
self.inv_db = cluster["discord"]
self.inv_collection = db["inventory"]

#SQLITE
try:
    connection = sqlite3.connect("./pets.sqlite")
    cursor = connection.cursor()
    print("Connection successful!")
except Error:
    print(Error)

pets = [{"name":"cat", "price":8000},
        {"name":"owl", "price":12000},
        {"name":"parrot", "price":15000},
        {"name":"dog", "price":18000},
        {"name":"wolf", "price":25000},
        {"name":"snake", "price":28000},
        {"name":"heron", "price":30000},
        {"name":"mongoose", "price":40000},
        {"name":"eagle", "price":43000},
        {"name":"fox", "price":45000}]

prey = [{"name":"rats", "price":8000},
        {"name":"lizzards", "price":12000},
        {"name":"moles", "price":15000},
        {"name":"beetles", "price":18000},
        {"name":"bread", "price":25000},
        {"name":"rabbits", "price":28000},
        {"name":"fish", "price":30000},
        {"name":"tiny cat", "price":40000}]

class Pets(commands.Cog):
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
        petexists = cursor.execute("SELECT * FROM pets WHERE id=?", (ctx.author.id, )).fetchone()
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
        if not petexists:
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
        else:
            await ctx.send("Hey you already own a pet dont ya. Leave that pet if you want another one!")



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

    @tasks.loop(seconds=3600)
    async def petloop(self):
        newhealth = cursor.execute("UPDATE pets SET health=health-1")
        newlove = cursor.execute("UPDATE pets SET love=love-1")
        newhunger = cursor.execute("UPDATE pets SET hunger=hunger-1")
        fun = cursor.execute("UPDATE pets SET fun=fun-1")
        connection.commit()

    @commands.Cog.listener()
    async def on_ready(self):
        self.petloop.start()
        print("Animal Loop started!")

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
            if expense > wallet:
                await ctx.send(f"You don't have enough money in your wallet to buy some food for {etinfo}! So sad!")
            else:
                await ctx.send(f"You bought food and water for {etinfo} and it cost you {expense} coins but increased {etinfo}'s health by 5 points! cool!")
                collection.update_one({"user":ctx.author.id}, {"$set":{"wallet":wallet-expense}})
                cursor.execute("UPDATE pets SET health=health+5")
                cursor.execute("UPDATE pets SET exp=exp+5")

    @commands.command()
    async def petleave(self, ctx):
        petinfo = cursor.execute("SELECT * FROM pets WHERE id=?", (ctx.author.id,))
        if not petinfo:
            await ctx.send("What the hell dont troll me. You don't even have a pet!")
        else:
            await ctx.send("Do you really want to leave your pet alone and move on?! **REPLY WITH `yes` OR  `no`**")
            def check(m):
                return m.author == ctx.author
            msg = await self.bot.wait_for('message', check=check)
            if msg.content == 'yes':
                await ctx.send("So shameful you left your pet!")
                cursor.execute("DELETE FROM pets WHERE id=?", (ctx.author.id,))
            elif msg.content == 'no':
                await ctx.send("Good so you are keeping your pet. But can;t you be firm with your decisions.")
            else:
                await ctx.send("I told you to respond with yes or no forget it now!")
            connection.commit()

    @commands.command()
    async def mypet(self, ctx):
        petcheck = cursor.execute("SELECT name FROM pets WHERE id=?", (ctx.author.id,)).fetchone()
        if not petcheck:
            await ctx.send("Buy a pet and then return!")
        else:
            pethealth = cursor.execute("SELECT health FROM pets WHERE id=?", (ctx.author.id,)).fetchone()
            petfun = cursor.execute("SELECT fun FROM pets WHERE id=?", (ctx.author.id,)).fetchone()
            petlove = cursor.execute("SELECT love FROM pets WHERE id=?", (ctx.author.id, )).fetchone()
            petexp = cursor.execute("SELECT experince FROM pets WHERE id=?", (ctx.author.id,)).fetchone()
            pethunger = cursor.execute("SELECT hunger FROM pets WHERE id=?", (ctx.author.id,)).fetchone()
            petlevel = cursor.execute("SELECT level FROM pets WHERE id=?", (ctx.author.id,)).fetchone()
            embed = discord.Embed(title=f"{petcheck[0]}'s Current Stats!", colour=discord.Colour.dark_green())
            embed.add_field(name=f"Hunger", value=f"{pethunger[0]}%")
            embed.add_field(name=f"Fun", value=f"{petfun[0]}%")
            embed.add_field(name="Love", value=f"{petlove[0]}%")
            embed.add_field(name="Health", value=f"{pethealth[0]}%")
            embed.add_field(name="Level", value=f"{petlevel[0]}")
            embed.add_field(name="Exp", value=f"{petexp[0]}")
            await ctx.send(embed=embed)
            updates = cursor.execute("UPDATE pets SET experince=experince+8 WHERE id=?", (ctx.author.id,))
            connection.commit()

    @tasks.loop(seconds=700)
    async def expchecker(self, ctx):
        exp = 0
        check = cursor.execute("SELECT experince, name FROM pets WHERE experince>=100").fetchone()
        if not check:
            return
        elif check:
            await ctx.send(f"Hey {check[1]} is now on next level. Hooray! Looks like you have taken good care of it.")
            cursor.execute("UPDATE pets SET experince=? WHERE id=?", (exp, ctx.author.id))
            cursor.execute("UPDATE pets SET level=level+1 WHERE id=?", (ctx.author.id,))

    @commands.command(help = "use this to make your pet hunt for you. The pet will hunt food and animals for you. You can sell these in the market")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 3600, BucketType.user)
    async def pethunt(self, ctx):
        check = cursor.execute("SELECT pet_type, level, name FROM pets WHERE id=?", (ctx.author.id,)).fetchone()
        if not check:
            await ctx.send("If you dont have a pet, how can you go hunting with it??!")
        else:
            pet = check[0]
            level = check[1]
            name = check[2]
            if pet == 'cat':
                if level < 11:
                    prey = random.choice(['rats', 'lizzards', 'moles'])
                    n = random.randrange(2, 3)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
                elif level > 10 and level < 21:
                    prey = random.choice(['rats', 'lizzards', 'moles'])
                    n = random.randrange(4, 5)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
                elif level > 20 and level < 31:
                    prey = random.choice(['rats', 'lizzards', 'moles'])
                    n = random.randrange(6, 7)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
                elif level > 30 and level < 41:
                    prey = random.choice(['rats', 'lizzards', 'moles'])
                    n = random.randrange(8, 9)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
                elif level > 40 and level < 51:
                    prey = random.choice(['rats', 'lizzards', 'moles', 'rabbits'])
                    n = random.randrange(10, 11)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
                elif level > 50 and level < 61:
                    prey = random.choice(['rats', 'lizzards', 'moles', 'rabbits'])
                    n = random.randrange(12, 13)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
                elif level > 60 and level < 71:
                    prey = random.choice(['rats', 'lizzards', 'moles', 'rabbits'])
                    n = random.randrange(14, 15)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
                elif level > 70 and level < 81:
                    prey = random.choice([ 'lizzards', 'moles', 'rabbits', 'fish'])
                    n = random.randrange(5, 12)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
                elif level > 80 and level < 91:
                    prey = random.choice(['moles', 'rabbits', 'fish'])
                    n = random.randrange(8, 15)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
                elif level > 90 and level < 101:
                    prey = random.choice(['rabbits', 'fish'])
                    n = random.randrange(10, 20)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
            elif pet == 'owl':
                if level < 11:
                    prey = random.choice(['rats', 'beetles', 'moles','lizzards'])
                    n = random.randrange(2, 3)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
                elif level > 10 and level < 21:
                    prey = random.choice(['rats', 'beetles', 'moles','lizzards'])
                    n = random.randrange(4, 5)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
                elif level > 20 and level < 31:
                    prey = random.choice(['rats', 'lizzards', 'moles', "beetles"])
                    n = random.randrange(6, 7)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
                elif level > 30 and level < 41:
                    prey = random.choice(['rats', 'lizzards', 'moles',"beetles"])
                    n = random.randrange(8, 9)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
                elif level > 40 and level < 51:
                    prey = random.choice(['rats', 'lizzards', 'moles', 'rabbits',"beetles"])
                    n = random.randrange(10, 11)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
                elif level > 50 and level < 61:
                    prey = random.choice(['rats', 'lizzards', 'moles', 'rabbits', "beetles"])
                    n = random.randrange(12, 13)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
                elif level > 60 and level < 71:
                    prey = random.choice(['rats', 'lizzards', 'moles', 'rabbits', "beetles"])
                    n = random.randrange(14, 15)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
                elif level > 70 and level < 81:
                    prey = random.choice(['moles', 'rabbits', "beetles", 'fish'])
                    n = random.randrange(5, 12)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
                elif level > 80 and level < 91:
                    prey = random.choice(['rats','rabbits', 'fish'])
                    n = random.randrange(8, 15)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
                elif level > 90 and level < 101:
                    prey = random.choice(['rabbits', 'fish', "tiny cat"])
                    n = random.randrange(10, 20)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
            elif pet == 'parrot':
                if level < 11:
                    prey = random.choice(['bread','beetles', 'moles','lizzards'])
                    n = random.randrange(3, 4)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
                elif level > 10 and level < 21:
                    prey = random.choice(['bread', 'beetles', 'moles','lizzards'])
                    n = random.randrange(5, 6)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
                elif level > 20 and level < 31:
                    prey = random.choice(['bread', 'lizzards', 'moles', "beetles"])
                    n = random.randrange(7, 8)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
                elif level > 30 and level < 41:
                    prey = random.choice(['bread', 'lizzards', 'moles',"beetles"])
                    n = random.randrange(9, 10)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
                elif level > 40 and level < 51:
                    prey = random.choice(['bread', 'lizzards', 'moles', 'rabbits',"beetles"])
                    n = random.randrange(11, 12)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
                elif level > 50 and level < 61:
                    prey = random.choice(['bread' , 'lizzards', 'moles', 'rabbits', "beetles"])
                    n = random.randrange(13, 14)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
                elif level > 60 and level < 71:
                    prey = random.choice(['bread', 'lizzards', 'moles', 'rabbits', "beetles"])
                    n = random.randrange(15, 16)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
                elif level > 70 and level < 81:
                    prey = random.choice(['bread', 'rabbits', "beetles", 'fish'])
                    n = random.randrange(6, 13)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
                elif level > 80 and level < 91:
                    prey = random.choice(['bread','rabbits', 'fish'])
                    n = random.randrange(9, 16)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})
                elif level > 90 and level < 101:
                    prey = random.choice(['rabbits', 'fish', "tiny cat"])
                    n = random.randrange(11, 21)
                    await ctx.send(f"You went hunting with {name} and fought with {n} {prey} and caught them, they are in your inventory now!")
                    inv_collection.update_one({"user":ctx.author.id}, {"$inc":{prey:n}})



    @commands.command(help = "list of prey and how much money you get if you sell them")
    @commands.guild_only()
    async def preylist(self, ctx):
        embed = discord.Embed(title=f"{self.bot.user}'s Pet Shop!", colour=discord.Colour.blue())
        for item in prey:
            name = item["name"]
            price = item["price"]
            embed.add_field(name=f'**{name}**', value=f"{price}", inline=False)
            embed.set_footer(text="To sell prey use %sellprey 'prey'")
        await ctx.send(embed=embed)






    @commands.Cog.listener()
    async def on_ready(self):
        self.expchecker.start()
        print("Checking for exp now...")




def setup(bot):
    bot.add_cog(Pets(bot))
