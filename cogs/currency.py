import discord
from discord.ext import commands
import random
import os
from discord.ext.commands.cooldowns import BucketType
import pymongo
from pymongo import MongoClient
import asyncio

#MONGODB
cluster = MongoClient("mongodb+srv://Admin-MyName:Parth!7730@my-dbs.xlx4y.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["discord"]
collection = db["user_data"]
inv_db = cluster["discord"]
inv_collection = db["inventory"] 

#SHOP
mainshop = [{"name": "watch", "price": 2000, "description": "Show off your watch to all!, However its just useless"},
            {"name": "fishing_rod", "price": 10000,
             "description": "Helps you in fishing you can use the #fish command if you have a fishing rod!"},
            {"name": "second_hand_laptop", "price": 11000,
             "description": "Just a second hand laptop which might be in your budget"},
            {"name": "fidget_spinner", "price": 2000,
             "description": "Spin it the fastest you can!"},
            {"name": "mobile_phone", "price": 7000,
             "description": "Just an amazing mobile phone but who cares its just for show off"},
            {"name": "bag_lock", "price": 13000, "description": "Nobody can rob you if you have even one of these"},
            {"name":"hunting_rifle", "price":9000, "description":"Use it to show off and also for the `%hunt` command!"},
            {"name":"apple", "price":25, "description":"An apple a day keeps the doctor away. Eat an apple and feel better!"},
            {"name":"cookie", "price":15, "description":"A good mouth blending cookie!"}]



class Currency(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def balance(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        bankinfo = collection.find_one({"user": member.id})
        if not bankinfo:
        #make new entry
            collection.insert_one({"user": member.id, "wallet": 0, "bank": 0})
            inv_collection.insert_one({"user":ctx.author.id, "watch":0, "second_hand_laptop":0, "hunting_rifle":0, "fidget_spinner":0, "fishing_rod":0, "mobile_phone":0, "bag_lock":0, "apple":0, "cookie":0})
            await ctx.send(f'{member.name} opening new bank account for you as you dont have one yet.')
            return
        else:
            # print(f'bankinfo : {bankinfo}')
            wallet = bankinfo['wallet']
            bank = bankinfo['bank']
            net_worth = wallet + bank
            embed = discord.Embed(title=f"{member.name}'s balance", description=f"**WALLET:** {wallet}\n**BANK:** {bank}\n**NET WORTH:** {net_worth}", colour=discord.Colour.blue())
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @commands.command()
    async def beg(self, ctx):
        bankinfo = collection.find_one({"user": ctx.author.id})
        if not bankinfo:
            #make new entry
            collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0})
            inv_collection.insert_one({"user": ctx.author.id, "watch": 0, "second_hand_laptop": 0, "hunting_rifle": 0,
                                       "fidget_spinner": 0, "fishing_rod": 0, "mobile_phone": 0, "bag_lock": 0, "apple": 0, "cookie": 0})
            await ctx.send(f'{ctx.author.name} opening new bank account for you as you dont have one yet. Please use the beg command again after that!')
            return
        else:
            payer = random.choice(['Deadpool', 'Wolverine', 'Dwighit Schrute', 'The guy you Hate the Most', 'Your Friend'])
            earning = random.randrange(0, 500)
            update = collection.update_one({"user": ctx.author.id}, {"$inc": {"wallet": earning}})
            await ctx.send(f"You got {earning} coins from {payer}")


    @commands.command(aliases=['dep'])
    async def deposit(self, ctx, amount: int=None):
        bankinfo = collection.find_one({"user": ctx.author.id})
        if not bankinfo:
            #make new entry
            collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0})
            inv_collection.insert_one({"user": ctx.author.id, "watch": 0, "second_hand_laptop": 0, "hunting_rifle": 0,
                                       "fidget_spinner": 0, "fishing_rod": 0, "mobile_phone": 0, "bag_lock": 0, "apple": 0, "cookie": 0})
            await ctx.send(f'{ctx.author.name} opening new bank account for you as you dont have one yet! Actually I am thinking what were you depositing if you had no account nor money?!')
            return
        else:
            if amount == None:
                await ctx.reply("You have to send the amount to be deposited with the command!")
            elif amount != None:
                wallet = bankinfo['wallet']
                if amount > wallet:
                    await ctx.send("You dont have that much money in your wallet so how can I deposit into your bank account?!")
                elif amount == 0:
                    await ctx.reply("Hey what you tryin to Bug me out?! **How can I deposit 0 coins?**")
                elif amount < 0:
                    await ctx.reply("This is too much! **I ain't depositing negative values!**")
                else:
                    new_wall_money = wallet-amount
                    new_wallet = collection.update_one({"user":ctx.author.id}, {"$set": {"wallet": new_wall_money}})
                    new_bank = collection.update_one({"user": ctx.author.id}, {"$inc": {"bank": amount}})
                    await ctx.send("Amount deposited to your bank account!")


    @commands.command(aliases=['with'])
    async def withdraw(self, ctx, amount: int=None):
        bankinfo = collection.find_one({"user": ctx.author.id})
        if not bankinfo:
            #make new entry
            collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0})
            inv_collection.insert_one({"user": ctx.author.id, "watch": 0, "second_hand_laptop": 0, "hunting_rifle": 0,
                                       "fidget_spinner": 0, "fishing_rod": 0, "mobile_phone": 0, "bag_lock": 0, "apple": 0, "cookie": 0})
            await ctx.send(f'{ctx.author.name} opening new bank account for you as you dont have one yet! Actually I am thinking from where were you withdrawing if you had no account nor money?!')
            return
        else:
            if amount == None:
                await ctx.reply("You have to send the amount to be withdrawed with the command!")
            elif amount != None:
                wallet = bankinfo["wallet"]
                bank = bankinfo["bank"]
                if amount > bank:
                    await ctx.send("You dont have that much money in your bank account so how can I withdraw from your bank account?!")
                elif amount == 0:
                    await ctx.send("Nice try kiddo! **Not gonna withdraw 0 coins from your bank account!**")
                elif amount < 0:
                    await ctx.send("The amount to be withdrawed should be positive! **C'mon man so stupid!**")
                else:
                    new_bank_money = bank-amount
                    new_wallet = collection.update_one({"user":ctx.author.id}, {"$inc":{"wallet": amount}})
                    new_bank = collection.update_one({"user":ctx.author.id}, {"$set": {"bank":new_bank_money}})
                    await ctx.send("Withdrawed the amount from your bank account to your wallet!")

    
    @commands.command()
    async def slots(self, ctx, amount: int=None):
        bankinfo = collection.find_one({"user":ctx.author.id})
        if not bankinfo:
            await ctx.send("Creating an account for you as you dont have one!")
            collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0})
            inv_collection.insert_one({"user": ctx.author.id, "watch": 0, "second_hand_laptop": 0, "hunting_rifle": 0,
                                       "fidget_spinner": 0, "fishing_rod": 0, "mobile_phone": 0, "bag_lock": 0, "apple": 0, "cookie": 0})
            return
        else:
            wallet = bankinfo["wallet"]
            if amount == None:
                await ctx.send("You have to bet something to play slots!")
            elif amount > wallet:
                await ctx.send("You dont have that much money to bet!")
            elif amount < 0:
                await ctx.send("You cant bet negative amounts!")
            else:
                final = []
                for i in range(3):
                    a = random.choice([":poop:", ":smile:", ":shower:", ":cherry_blossom:"])
                    final.append(a)
                await ctx.send(str(final))
                if final[0] == final[1] or final[0] == final[2] or final[2] == final[1]:
                    earning = amount*2
                    new_wallet = collection.update_one({"user":ctx.author.id}, {"$inc":{"wallet":earning}})
                    await ctx.send("You won!")
                else:
                    loss = amount/2
                    current = wallet-loss
                    new_wallet_loss = collection.update_one({"user":ctx.author.id}, {"$set":{"wallet":current}})
                    await ctx.send("You lost!")


    @commands.command()
    async def pay(self, ctx, member: discord.Member=None, amount: int=None):
        bankinfo = collection.find_one({"user":ctx.author.id})
        wallet = bankinfo['wallet']
        mem_bankinfo = collection.find_one({"user":member.id})
        if not bankinfo:
            await ctx.send("Creating your account first as you don't have one!")
            collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0})
            inv_collection.insert_one({"user": ctx.author.id, "watch": 0, "second_hand_laptop": 0, "hunting_rifle": 0,
                                       "fidget_spinner": 0, "fishing_rod": 0, "mobile_phone": 0, "bag_lock": 0, "apple": 0, "cookie": 0})
            return
        elif not mem_bankinfo:
            await ctx.send(f"{member.mention}, doesnt have an account creating one for him!")
            collection.insert_one({"user": member.id, "wallet": 0, "bank": 0})
            inv_collection.insert_one({"user": member.id, "watch": 0, "second_hand_laptop": 0, "hunting_rifle": 0,
                                       "fidget_spinner": 0, "fishing_rod": 0, "mobile_phone": 0, "bag_lock": 0, "apple": 0, "cookie": 0})
            mem_wallet = mem_bankinfo['bank']
            return
        else:
            if member == None:
                await ctx.send("You have to mention someone in order to pay him/her!")
            elif member != None:
                if amount == None:
                    await ctx.send("Cant pay the person nothing!")
                elif amount > wallet:
                    await ctx.send("You dont have that much money to pay the person")
                elif amount < 0:
                    await ctx.send("You cant pay negative amounts!")
                elif amount != None:
                    await ctx.send("Ok paying!...")
                    new_wallet = wallet-amount
                    collection.update_one({"user":ctx.author.id}, {"$set": {"wallet":new_wallet}})
                    collection.update_one({"user":member.id}, {"$inc":{"bank":amount}})
                    await asyncio.sleep(2)
                    await ctx.send(f"Payed the amount from your wallet to {member.mention}'s bank account!")



    @commands.command(aliases=['pm', 'postmemes'])
    async def postmeme(self, ctx):
        bankinfo = collection.find_one({"user":ctx.author.id})
        if not bankinfo:
            await ctx.send("You dont have an account creating one for you!...")
            collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0})
            inv_collection.insert_one({"user": ctx.author.id, "watch": 0, "second_hand_laptop": 0, "hunting_rifle": 0,
                                       "fidget_spinner": 0, "fishing_rod": 0, "mobile_phone": 0, "bag_lock": 0, "apple": 0, "cookie": 0})
            return
        else:
            earning = random.randrange(1, 1000)
            await ctx.send(f"{ctx.author.mention}, **__What Type of Meme Do You Want To Post?__**\n``f``: **Fresh Meme**\n``r``: **Reposted Meme**\n``i``: **Intellectual Meme**\n``c``: **Copypasted Meme**\n``k``: **Kind Meme**")
            def check(m):
                return m.content == 'f', 'i', 'c', 'r', 'k' and m.channel == ctx.channel
            await self.bot.wait_for('message', check=check, timeout=30)
            if earning < 500:
                await ctx.send(f"You earned a decent response from the internet regarding the meme. So you get **{earning}**")
                collection.update_one({"user":ctx.author.id}, {"$inc":{"wallet":earning}})
            elif earning < 1000:
                await ctx.send(f"You earned a fairly good response from the internet regarding the meme. So you get **{earning}**")
                collection.update_one({"user": ctx.author.id}, {"$inc": {"wallet": earning}})


    @commands.command()
    async def shop(self, ctx):
        bankinfo = collection.find_one({"user":ctx.author.id})
        if not bankinfo:
            await ctx.send("You dont have an account creating one for you!...")
            collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0})
            inv_collection.insert_one({"user": ctx.author.id, "watch": 0, "second_hand_laptop": 0, "hunting_rifle": 0, "fidget_spinner": 0, "fishing_rod": 0, "mobile_phone": 0, "bag_lock": 0, "apple": 0, "cookie": 0})
            return
        else:
            embed = discord.Embed(title=f"**{self.bot.user}'s shop**", colour=discord.Colour.red())
            for item in mainshop:
                name = item["name"]
                price = item["price"]
                description = item["description"]
                embed.add_field(name=f'**{name}--${price}**',value=f'description: {description}', inline=False)
                embed.set_footer(text="To buy something use %buy 'Thing'")
            await ctx.send(embed=embed)


    @commands.command()
    async def buy(self, ctx, item, amount=1):
        author_inv = inv_collection.find_one({"user":ctx.author.id})
        author_bank = collection.find_one({"user":ctx.author.id})
        if not author_bank:
            await ctx.send("You dont have an account creating one for you!...")
            collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0})
            inv_collection.insert_one({"user": ctx.author.id, "watch": 0, "second_hand_laptop": 0, "hunting_rifle": 0,"fidget_spinner": 0, "fishing_rod": 0, "mobile_phone": 0, "bag_lock": 0, "apple": 0, "cookie": 0})
            return
        else:
            wallet = author_bank["wallet"]
            if item in mainshop:
                price = item['price']
                if wallet < price:
                    await ctx.reply("You don't have that much money!")
                else:
                    new_wall_amt = wallet-price
                    new_wallet = collection.update_one({"user":ctx.author.id}, {"$set":{"wallet":new_wall_amt}})
                    item_inv = author_inv[item]
                    new_inv = inv_collection.update_one({"user":ctx.author.id}, {"$inc": {item_inv:amount}})
                    await ctx.send(f"Oh you bought {amount}, {item}")





def setup(bot):
    bot.add_cog(Currency(bot))
