from discord import channel
from cogs.utility import check
import discord
from discord import user
from discord.ext import commands, tasks
import random
import os
from discord.ext.commands.cooldowns import BucketType
import pymongo
from pymongo import MongoClient
import asyncio
import sqlite3
from sqlite3 import Error
from itertools import cycle

#SQLITE3
connection = sqlite3.connect("lottery.sqlite")
cursor = connection.cursor()

#MONGODB
cluster = MongoClient("mongodb+srv://Admin-MyName:Parth!7730@my-dbs.xlx4y.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["discord"]
collection = db["user_data"]
inv_db = cluster["discord"]
inv_collection = db["inventory"]

#MAIN SHOP
mainshop = [{"name": "watch", "price": 2000, "description": "Show off your watch to all!, However its just useless"},
            {"name": "fishing_rod", "price": 10000,
             "description": "Helps you in fishing you can use the #fish command if you have a fishing rod!"},
            {"name": "second_hand_laptop", "price": 11000,
             "description": "Just a second hand laptop which might be in your budget"},
            {"name": "fidget_spinner", "price": 2000,
             "description": "Spin it the fastest you can!"},
            {"name": "mobile_phone", "price": 7000,
             "description": "Just an amazing mobile phone which can be used for sending messages or for calling the devs or police in case of robbery!"},
            {"name": "bag_lock", "price": 13000, "description": "Nobody can rob you if you have even one of these"},
            {"name":"hunting_rifle", "price":9000, "description":"Use it to show off and also for the `%hunt` command!"},
            {"name":"apple", "price":25, "description":"An apple a day keeps the doctor away. Eat an apple and feel better!"},
            {"name":"cookie", "price":15, "description":"A good mouth blending cookie!"}]


#CHECKS
def pm_check(ctx):
    author_inv = inv_collection.find_one({"user":ctx.author.id})
    laptop_amt = author_inv['second_hand_laptop']
    if laptop_amt > 0:
        return True
    else:
        return False

def fish_check(ctx):
    author_inv = inv_collection.find_one({"user":ctx.author.id})
    fish_amt = author_inv['fishing_rod']
    if fish_amt > 0:
        return True
    else:
        return False

def hunt_check(ctx):
    author_inv = inv_collection.find_one({"user":ctx.author.id})
    rifle_amt = author_inv['hunting_rifle']
    if rifle_amt > 0:
        return True
    else:
        return False

class Currency(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Use the command to check your balance or mention someone to check theirs(maybe check for robbing them):smile:", aliases=['bal'])
    @commands.guild_only()
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
            embed = discord.Embed(title=f"{member.name}'s balance", description=f"\n\n**WALLET:** {wallet}\n**BANK:** {bank}\n**NET WORTH:** {net_worth}", colour=discord.Colour.blue())
            embed.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=embed)

    @commands.command(help="Use the command to beg. Exactly like a begger :laughing:")
    @commands.guild_only()
    @commands.cooldown(1, 65, BucketType.user)
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

    @beg.error
    async def beg_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            err = error.retry_after
            await ctx.send(f"Please try begging only after {round(err)} more seconds!")


    @commands.command(aliases=['dep'], help="Use the command to deposit some money from your wallet to your bank account!")
    @commands.guild_only()
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


    @commands.command(aliases=['with'], help="Use the command for withdrawing some money from your bank account to your wallet!")
    @commands.guild_only()
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

    
    @commands.command(help="Use the command to play slots with the bot! Intresting isn't it?!")
    @commands.guild_only()
    @commands.cooldown(1, 30, BucketType.user)
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

    @slots.error
    async def slots_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            err = error.retry_after
            await ctx.send(f"Hey how much slots will you play, Please try the command only after {round(err)} more seconds!")


    @commands.command(help="Use the command to pay some money to somebody! Maybe your friend by mentioning them!", aliases=['gift'])
    @commands.guild_only()
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



    @commands.command(aliases=['pm', 'postmemes'], help="Use your laptop(if you have) to post some memes on the internet you might earn some money!")
    @commands.check(pm_check)
    @commands.guild_only()
    @commands.cooldown(1, 45, BucketType.user)
    async def postmeme(self, ctx):
        bankinfo = collection.find_one({"user":ctx.author.id})
        if not bankinfo:
            await ctx.send("You don't have an account, creating one for you!...")
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

    @postmeme.error
    async def postmeme_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You need to buy a laptop for posting memes on the internet! Buy it using `%buy second_hand_laptop`")
        elif isinstance(error, commands.CheckFailure):
            await ctx.send("Hey you should have a laptop for posting memes. Buy one from the shop!")

    @commands.command()
    @commands.cooldown(1, 86400, BucketType.user)
    @commands.guild_only()
    async def daily(self, ctx):
        bankinfo = collection.find_one({"user": ctx.author.id})
        if not bankinfo:
            await ctx.send("You don't have an account, creating one for you!...")
            collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0})
            inv_collection.insert_one({"user": ctx.author.id, "watch": 0, "second_hand_laptop": 0, "hunting_rifle": 0,"fidget_spinner": 0, "fishing_rod": 0, "mobile_phone": 0, "bag_lock": 0, "apple": 0, "cookie": 0})
            return
        else:
            earning = random.randrange(7500, 10000)
            await ctx.send(f"Hey {ctx.author.mention}, here is your daily money you got {earning} coins!")
            collection.update_one({"user":ctx.author.id}, {"$inc":{"wallet":earning}})

    @daily.error
    async def daily_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            err = error.retry_after
            await ctx.send(f"Hey Hey you will get more money after {round(err)} more seconds! You got that right?")

    
    @commands.command(aliases=['cast'], help="Its time to use your fishing rod for fishing. Interesting but please do buy a fishing rod first!")
    @commands.check(fish_check)
    @commands.guild_only()
    @commands.cooldown(1, 60, BucketType.user)
    async def fish(self, ctx):
        bankinfo = collection.find_one({"user":ctx.author.id})
        if not bankinfo:
            await ctx.send("You don't have an account, creating one for you!...")
            collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0})
            inv_collection.insert_one({"user": ctx.author.id, "watch": 0, "second_hand_laptop": 0, "hunting_rifle": 0, "fidget_spinner": 0, "fishing_rod": 0, "mobile_phone": 0, "bag_lock": 0, "apple": 0, "cookie": 0})
            return
        else:
            fish_type = random.choices(['common fish', 'rare fish', 'epic fish', 'legendary fish'], weights=[85, 10, 3, 2])
            indexed_fish = fish_type[0]
            amount_fish = random.randrange(1, 5)
            await ctx.send(f"Hey you went fishing and got {amount_fish}, {fish_type[0]}")
            inv_collection.update_one({"user":ctx.author.id}, {"$inc": {indexed_fish:amount_fish}})

    @fish.error
    async def fish_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You need to buy a fishing rod for fishing! Buy one from the shop!")
        elif isinstance(error, commands.CommandOnCooldown):
            error_time = error.retry_after
            abs_time = round(error_time)
            await ctx.send(f"**Whoa to fast right?!** You have to wait {abs_time} more before you use the command!")


    @commands.command(aliases=['hl', 'bigsmall'], help="Use the command to play a highlow game with the bot and earn some money!")
    @commands.guild_only()
    @commands.cooldown(1, 50, BucketType.user)
    async def highlow(self, ctx):
        bankinfo = collection.find_one({"user":ctx.author.id})
        if not bankinfo:
            await ctx.send("You don't have an account, creating one for you!...")
            collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0})
            inv_collection.insert_one({"user": ctx.author.id, "watch": 0, "second_hand_laptop": 0, "hunting_rifle": 0,"fidget_spinner": 0, "fishing_rod": 0, "mobile_phone": 0, "bag_lock": 0, "apple": 0, "cookie": 0})
            return
        else:
            correct_no = random.randrange(1, 100)
            hint_no = random.randrange(1, 100)
            earning = random.randrange(150, 950)
            wallet = bankinfo['wallet']
            embed = discord.Embed(title=f"{ctx.author.name}'s High-Low Game!", description=f"A secret number between 1-100 has been chosen your hint is **{hint_no}**. Respond with **high**, **low** or **jackpot**")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_footer(text="Think whether the correct no is higher, lower or same as the hint no!")
            await ctx.send(embed=embed)
            def check(m):
                return m.channel == ctx.channel
            msg = await self.bot.wait_for('message', check=check, timeout=15.0)
            if msg.content == 'high':
                if hint_no < correct_no:
                    embed = discord.Embed(title=f"{ctx.author.name}'s Winning High-Low Game!", description=f"**You won {earning} coins!**", colour=discord.Colour.green())
                    embed.set_thumbnail(url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                    collection.update_one({"user":ctx.author.id}, {"$inc":{"wallet":earning}})
                elif hint_no > correct_no:
                    embed = discord.Embed(title=f"{ctx.author.name}'s Losing High-Low Game!",description=f"**The correct no was {correct_no} while you told high**", colour=discord.Colour.red())
                    embed.set_thumbnail(url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                elif hint_no == correct_no:
                    embed = discord.Embed(title=f"{ctx.author.name}'s Losing High-Low Game!",description=f"**The correct no was {correct_no} while you told high**", colour=discord.Colour.red())
                    embed.set_thumbnail(url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
            elif msg.content == 'low':
                if hint_no > correct_no:
                    embed = discord.Embed(title=f"{ctx.author.name}'s Winning High-Low Game!",description=f"**You won {earning} coins!**", colour=discord.Colour.green())
                    embed.set_thumbnail(url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                    collection.update_one({"user": ctx.author.id}, {
                                          "$inc": {"wallet": earning}})
                elif hint_no < correct_no:
                    embed = discord.Embed(title=f"{ctx.author.name}'s Losing High-Low Game!",description=f"**The correct no was {correct_no} while you told low**", colour=discord.Colour.red())
                    embed.set_thumbnail(url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                elif hint_no == correct_no:
                    embed = discord.Embed(title=f"{ctx.author.name}'s Losing High-Low Game!",description=f"**The correct no was {correct_no} while you told low**", colour=discord.Colour.red())
                    embed.set_thumbnail(url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
            elif msg.content == 'jackpot':
                if hint_no == correct_no:
                    embed = discord.Embed(title=f"{ctx.author.name}'s Winning High-Low Game!",
                                        description=f"**You won {earning} coins!**", colour=discord.Colour.green())
                    embed.set_thumbnail(url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                    collection.update_one({"user": ctx.author.id}, {
                                          "$inc": {"wallet": earning}})
                elif hint_no < correct_no:
                    embed = discord.Embed(title=f"{ctx.author.name}'s Losing High-Low Game!",
                                        description=f"**The correct no was {correct_no} while you told jackpot**", colour=discord.Colour.red())
                    embed.set_thumbnail(url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                elif hint_no > correct_no:
                    embed = discord.Embed(title=f"{ctx.author.name}'s Losing High-Low Game!",
                                        description=f"**The correct no was {correct_no} while you told jackpot**", colour=discord.Colour.red())
                    embed.set_thumbnail(url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)

    @highlow.error
    async def highlow_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            err = error.retry_after
            await ctx.send(f"If you play so much highlow, you will get high yourself. Please use the command only after {round(err)} more seconds!")

    
    @commands.command(help="Use the command for robbing someone! Be careful sometimes they might have bag locks!", aliases=['steal'])
    @commands.cooldown(1, 70, BucketType.user)
    async def rob(self, ctx, member: discord.Member = None):
        if member == None:
            await ctx.send("You have to mention someone to rob! Otherwise I will rob you")
        else:
            bankinfo = collection.find_one({"user":ctx.author.id})
            if not bankinfo:
                await ctx.send("Creating your account as it doesn't exist!")
                collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0})
                inv_collection.insert_one({"user": ctx.author.id, "watch": 0, "second_hand_laptop": 0, "hunting_rifle": 0,"fidget_spinner": 0, "fishing_rod": 0, "mobile_phone": 0, "bag_lock": 0, "apple": 0, "cookie": 0})
                return
            else:
                bank = collection.find_one({"user":member.id})
                if not bank:
                    await ctx.send("Creating your account as it doesn't exist!")
                    collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0})
                    inv_collection.insert_one({"user": ctx.author.id, "watch": 0, "second_hand_laptop": 0, "hunting_rifle": 0,"fidget_spinner": 0, "fishing_rod": 0, "mobile_phone": 0, "bag_lock": 0, "apple": 0, "cookie": 0})
                    return
                else:
                    wallet = bankinfo["wallet"]
                    mem_inv = inv_collection.find_one({"user":member.id})
                    mem_lock = mem_inv['bag_lock']
                    earnings = 3/10*bank["wallet"]
                    mem_wallet = bank["wallet"]
                    e = 3/10*wallet
                    if mem_lock > 0:
                        msg1 = await ctx.send("Oops you got caught! The member has a bag lock enabled!")
                        await asyncio.sleep(2)
                        await msg1.edit(content = "Now he will steal money from you! :smile:")
                        await asyncio.sleep(2)
                        await msg1.edit(content=f"{member} stole {round(e)} from {ctx.author}!")
                        collection.update_one({"user":member.id}, {"$inc":{"wallet":round(e)}})
                        collection.update_one({"user":ctx.author.id}, {"$set":{"wallet":round(wallet-e)}})
                        inv_collection.update_one({"user":member.id}, {"$set":{"bag_lock":mem_lock-1}})
                    else:
                        msg = await ctx.send(f"Hey you got away with {round(earnings)} from {member.name}'s wallet!")
                        collection.update_one({"user":ctx.author.id}, {"$inc":{"wallet":round(earnings)}})
                        collection.update_one({"user":member.id}, {"$set":{"wallet":round(mem_wallet-earnings)}})

    @rob.error
    async def rob_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            e = error.retry_after
            await ctx.send(f"You can rob someone only after {round(e)} more seconds!")     
        else:
            await ctx.send("There was an error executing the command try contacting the devs if you want!")               



    @commands.command(help="Bet something and try to win Loser!", aliases=['gamble'])
    @commands.cooldown(1, 40, BucketType.user)
    async def bet(self, ctx, amount:int):
        bankinfo = collection.find_one({"user":ctx.author.id})
        if not bankinfo:
            await ctx.send("Creating your account as it doesn't exist!")
            collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0})
            inv_collection.insert_one({"user": ctx.author.id, "watch": 0, "second_hand_laptop": 0, "hunting_rifle": 0,"fidget_spinner": 0, "fishing_rod": 0, "mobile_phone": 0, "bag_lock": 0, "apple": 0, "cookie": 0})
            return
        else:
            wallet = bankinfo["wallet"]
            bot_dice = random.randrange(2, 12)
            user_dice = random.randrange(2, 12)
            if amount < 50:
                await ctx.send("The amount should be more than 50!")
            elif amount > wallet:
                await ctx.send("You don't have enough money in your wallet!")
            else:
                multiplier = random.randrange(1, 100)
                loss = multiplier/100*amount
                won = multiplier/100*amount
                if bot_dice > user_dice:
                    NEW_BALANCE = wallet-loss
                    embed = discord.Embed(title=f"{ctx.author.name}'s Losing Bet!", description=f"You Lost {loss} coins\n\n**Percent Lost: **{multiplier}%\n**New Balance: **{NEW_BALANCE}", colour=discord.Colour.red())
                    embed.add_field(name=f"{ctx.author.name} Rolled:", value=f"{user_dice}")
                    embed.add_field(name=f"{self.bot.user}", value=f"{bot_dice}")
                    embed.set_image(url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                    collection.update_one({"user":ctx.author.id}, {"$set":{"wallet":NEW_BALANCE}})
                elif bot_dice < user_dice:
                    NEW_BALANCE = wallet+won
                    embed = discord.Embed(title=f"{ctx.author.name}'s Winning Bet!",description=f"You Won {won} coins\n\n**Percent Lost: **{multiplier}%\n**New Balance: **{NEW_BALANCE}", colour=discord.Colour.green())
                    embed.add_field(name=f"{ctx.author.name} Rolled:", value=f"{user_dice}")
                    embed.add_field(name=f"{self.bot.user} Rolled:", value=f"{bot_dice}")
                    embed.set_image(url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                    collection.update_one({"user": ctx.author.id}, {"$inc": {"wallet": won}})
                elif bot_dice == user_dice:
                    await ctx.send(f"The bot rolled: {bot_dice} and {ctx.author.name} rolled: {user_dice} So its a tie nobody wins!")

    @bet.error
    async def bet_error(Self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            err = error.retry_after
            await ctx.send(f"Please dont bet so much or else i will make you lose on purpose. Please try the command only after {round(err)} more seconds!")

    @commands.command(help="Use the command to buy a lottery ticket! Winners are announced every hour!")
    @commands.guild_only()
    async def lottery(self, ctx):
        bankinfo = collection.find_one({"user":ctx.author.id})
        wallet = bankinfo["wallet"]
        if not bankinfo:
            await ctx.send("You don't have an account, creating one for you!...")
            collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0})
            inv_collection.insert_one({"user": ctx.author.id, "watch": 0, "second_hand_laptop": 0, "hunting_rifle": 0,"fidget_spinner": 0, "fishing_rod": 0, "mobile_phone": 0, "bag_lock": 0, "apple": 0, "cookie": 0})
            return
        else:
            await ctx.send("Do you want to actually purchase a lottery ticket for 100 coins. **REPLY WITH `yes` OR `no`!**")
            def check(m):
                return m.channel == ctx.channel
            msg = await self.bot.wait_for('message', check=check)
            if msg.content == 'yes':
                if wallet > 100:
                    ticket = random.randrange(1, 100000)
                    cursor.execute("""CREATE TABLE IF NOT EXISTS lottery (
                        name TEXT,
                        user_id INTEGER,
                        ticket_id INTEGER
                    );""")
                    cursor.execute("SELECT * FROM lottery WHERE user_id=?", (ctx.author.id,))
                    chec = cursor.fetchone()
                    if chec == True:
                        await ctx.send("You already have a ticket for this lottery!")
                    else:
                        ticket = random.randrange(1, 100000)
                        embed = discord.Embed(title="You have successfully purchased a lottery ticket!", description="The winners will be announced soon in [this server](https://discord.gg/27RSuxZSvj)")
                        await ctx.send(embed=embed)
                        collection.update_one({"user": ctx.author.id}, {"$set": {"wallet": wallet-100}})
                        cursor.execute("INSERT INTO lottery VALUES(?, ?, ?)", (ctx.author.name, ctx.author.id, ticket))
                        connection.commit()
                else:
                    await ctx.send("You need to have atleast 100 coins in your wallet to buy the ticket idiot!")            
            elif msg.content == "no":
                await ctx.send("Alright bro! Your wish!")

    @commands.command()
    async def mylotterytickets(self, ctx):
        lt = cursor.execute("SELECT * FROM lottery WHERE user_id=?", (ctx.author.id, )).fetchall()
        for tup in lt:
            no = len(lt)
        await ctx.send(f"You currently have {no} tickets for this up coming lottery!")


    @tasks.loop(seconds=3600)
    async def lotteryloop(self):
        lottery_channel = self.bot.get_channel(820600849982160907)
        earnings = random.randrange(100000, 500000)
        cursor.execute("SELECT * FROM lottery ORDER BY RANDOM() LIMIT 1")
        fetch = cursor.fetchone()
        cursor.execute("SELECT * FROM lottery")
        result = cursor.fetchall()
        ppl = len(result)
        name = fetch[0]
        user_id = fetch[1]
        userid = self.bot.get_user(user_id)
        ticket_id = fetch[2]
        embed = discord.Embed(title=f"WINNER - {name}", description=f"{name}---**{userid.mention}**---**TICKET ID={ticket_id}** won the lottery and walked away with {earnings}", colour=discord.Colour.gold())
        embed.set_footer(text="To buy your lottery ticket use the command %lottery, winners are announced each hour!")
        await lottery_channel.send(embed=embed)
        collection.update_one({"user":user_id}, {"$inc":{"bank":earnings}})
        cursor.execute("DELETE FROM lottery")
        connection.commit()

    
    @commands.Cog.listener()
    async def on_ready(self):
        self.lotteryloop.start()
        print("Lottery loop started!")

    @commands.command(help="Its time to use your hunting rifle if you have one to go and hunt animals! Cool", aliases=['hunting'])
    @commands.check(hunt_check)
    @commands.cooldown(1, 120, BucketType.user)
    async def hunt(self, ctx):
        animal_type = random.choices(['deer', 'bear', 'rabbit', 'raccoons', 'leapord', 'snake'], weights=[25, 10, 20, 30, 2, 13])
        animal_quantity = random.randrange(0, 8)
        await ctx.send(f"Hey you went hunting and got {animal_quantity} {animal_type[0]}!")
        inv_collection.update_one({"user":ctx.author.id}, {"$inc":{animal_type[0]:animal_quantity}})


    @hunt.error
    async def hunt_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            error_type = error.retry_after
            await ctx.send(f"Hey hey! You can go for hunting only after {round(error_type)} more seconds!")
        elif isinstance(error, commands.CheckFailure):
            await ctx.send("Hey you gotta have atleast one hunting rifle in your inventory for this!")

    @commands.command(help="Mention someone while using this command to rob their bank! Its tricky!")
    @commands.guild_only()
    @commands.cooldown(1, 400, BucketType.user)
    async def bankrob(self, ctx, member: discord.Member = None):
        if member == None:
            await ctx.reply("Please mention someone with the command so as to rob them")
        elif member != None:
            bankinfo = collection.find_one({"user":ctx.author.id})
            if not bankinfo:
                await ctx.send("You don't have an account, creating one for you!...")
                collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0})
                inv_collection.insert_one({"user": ctx.author.id, "watch": 0, "second_hand_laptop": 0, "hunting_rifle": 0,"fidget_spinner": 0, "fishing_rod": 0, "mobile_phone": 0, "bag_lock": 0, "apple": 0, "cookie": 0})
                return
            else:
                mem_bank = collection.find_one({"user":member.id})
                if not mem_bank:
                    await ctx.send("You don't have an account, creating one for you!...")
                    collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0})
                    inv_collection.insert_one({"user": ctx.author.id, "watch": 0, "second_hand_laptop": 0, "hunting_rifle": 0,"fidget_spinner": 0, "fishing_rod": 0, "mobile_phone": 0, "bag_lock": 0, "apple": 0, "cookie": 0})
                    return
                else:
                    bank = mem_bank['bank']
                    if bank > 2000:
                        earning = round(4/10*bank)
                        collection.update_one({"user":ctx.author.id}, {"$inc":{"bank":earning}})
                        collection.update_one({"user":member.id}, {"$set":{"bank":bank-earning}})
                        await ctx.reply(f"You stole a good amount. Your payout was {earning}")
                    else:
                        await ctx.reply("He doesn't even have 2000 coins. Why bankrob him?!")

    @bankrob.error
    async def bankrob_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            err = round(error.retry_after)
            await ctx.send(f"Why do you wanna rob everyone. Just stop you can rob someone only after {err} more seconds!")



    @commands.command(help="Use the command to check your inventory and check how much of a begger are you!!", aliases=['bag'])
    @commands.guild_only()
    async def inventory(self, ctx, member: discord.Member = None):
        if member == None:
            bankinfo = collection.find_one({"user":ctx.author.id})
            if not bankinfo:
                await ctx.send("You don't have an account, creating one for you!...")
                collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0})
                inv_collection.insert_one({"user": ctx.author.id, "watch": 0, "second_hand_laptop": 0, "hunting_rifle": 0,"fidget_spinner": 0, "fishing_rod": 0, "mobile_phone": 0, "bag_lock": 0, "apple": 0, "cookie": 0})
                return
            else:
                inventory = inv_collection.find_one({"user":ctx.author.id})
                embed = discord.Embed(title=f"{ctx.author.name}'s Inventory!", description="Owned Items", colour=discord.Colour.teal())
                for item in inventory:
                    items = inventory[item]
                    embed.add_field(name=f"{item}", value=f"{items}", inline=False)
                await ctx.send(embed=embed)
        else:
            bankinfo = collection.find_one({"user": member.id})
            if not bankinfo:
                await ctx.send(f"{member.name} doesnt have an account creating one for him!...")
                collection.insert_one({"user": member.id, "wallet": 0, "bank": 0})
                inv_collection.insert_one({"user": member.id, "watch": 0, "second_hand_laptop": 0, "hunting_rifle": 0,"fidget_spinner": 0, "fishing_rod": 0, "mobile_phone": 0, "bag_lock": 0, "apple": 0, "cookie": 0})
                return
            elif bankinfo:
                inventory = inv_collection.find_one({"user": member.id})
                embed = discord.Embed(title=f"{member.name}'s Inventory!", description="Owned Items", colour=discord.Colour.teal())
                for item in inventory:
                    items = inventory[item]
                    embed.add_field(name=f"{item}", value=f"{items}", inline=False)
                await ctx.send(embed=embed)

    @commands.command(help="Use this command to check out Blank-Chump's shop and maybe buy some items from there if you have the money!")
    @commands.guild_only()
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


    @commands.command(help="Use the command to buy some stuff from the shop! Anything if you can :thinking:")
    @commands.guild_only()
    async def buy(self, ctx, item, amount:int=1):
        author_inv = inv_collection.find_one({"user":ctx.author.id})
        author_bank = collection.find_one({"user":ctx.author.id})
        if not author_bank:
            await ctx.send("You dont have an account creating one for you!...")
            collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0})
            inv_collection.insert_one({"user": ctx.author.id, "watch": 0, "second_hand_laptop": 0, "hunting_rifle": 0,"fidget_spinner": 0, "fishing_rod": 0, "mobile_phone": 0, "bag_lock": 0, "apple": 0, "cookie": 0})
            return
        else:
            wallet = author_bank["wallet"]
            if item == 'watch':
                watch_price = 2000
                cost = watch_price*amount
                if wallet < cost:
                    await ctx.send("Hey you dont have that much money!")
                elif cost < wallet:
                    new_wallet_amt =  wallet-cost
                    author_inv_watch = inv_collection.update_one({"user":ctx.author.id}, {"$inc":{'watch':amount}})
                    author_wallet_watch = collection.update_one({"user":ctx.author.id}, {"$set":{"wallet":new_wallet_amt}})
                    await ctx.send(f"Ohh you have bought watch! for {cost}!")
                elif cost == wallet:
                    new_wallet_amt = wallet-cost
                    author_inv_watch = inv_collection.update_one({"user": ctx.author.id}, {"$inc": {'watch': amount}})
                    author_wallet_watch = collection.update_one({"user": ctx.author.id}, {"$set": {"wallet": new_wallet_amt}})
                    await ctx.send(f"Ohh you have bought watch! for {cost}!")
            elif item == 'second_hand_laptop':
                lap_price = 11000
                lap_cost = lap_price*amount
                if wallet < lap_cost:
                    await ctx.send("You don't have that much money in your wallet!")
                elif lap_cost < wallet:
                    new_wallet_amt = wallet-lap_cost
                    author_inv_lap = inv_collection.update_one({"user":ctx.author.id}, {"$inc":{'second_hand_laptop':amount}})
                    author_wallet_watch = collection.update_one({"user":ctx.author.id}, {"$set":{"wallet":new_wallet_amt}})
                    await ctx.send(f"Ohh you have bought Second Hand Laptop! for {lap_cost}!")
                elif lap_cost == wallet:
                    new_wallet_amt = wallet-lap_cost
                    author_inv_lap = inv_collection.update_one({"user": ctx.author.id}, {"$inc": {'second_hand_laptop': amount}})
                    author_wallet_watch = collection.update_one({"user": ctx.author.id}, {"$set": {"wallet": new_wallet_amt}})
                    await ctx.send(f"Ohh you have bought Second Hand Laptop! for {lap_cost}!")
            elif item == 'fishing_rod':
                fish_price = 10000
                fish_cost = fish_price*amount
                if wallet < fish_cost:
                    await ctx.send("You don't have enough money in your wallet!")
                elif fish_cost < wallet:
                    new_wallet_amt = wallet-fish_cost
                    author_inv_lap = inv_collection.update_one({"user": ctx.author.id}, {"$inc": {'fishing_rod': amount}})
                    author_wallet_watch = collection.update_one({"user": ctx.author.id}, {"$set": {"wallet": new_wallet_amt}})
                    await ctx.send(f"Ohh you have bought Fishing Rod! for {fish_cost}!")
                elif fish_cost == wallet:
                    new_wallet_amt = wallet-fish_cost
                    author_inv_lap = inv_collection.update_one({"user": ctx.author.id}, {"$inc": {'fishing_rod': amount}})
                    author_wallet_watch = collection.update_one({"user": ctx.author.id}, {"$set": {"wallet": new_wallet_amt}})
                    await ctx.send(f"Ohh you have bought Fishing Rod! for {fish_cost}!")
            elif item == 'fidget_spinner':
                spinner_price = 2000
                spinner_cost = spinner_price*amount
                if wallet < spinner_cost:
                    await ctx.send("You don't have enough money in your wallet!")
                elif spinner_cost < wallet:
                    new_wallet_amt = wallet-spinner_cost
                    author_inv_spin = inv_collection.update_one({"user": ctx.author.id}, {"$inc": {'fidget_spinner': amount}})
                    author_wallet_spin = collection.update_one({"user": ctx.author.id}, {"$set": {"wallet": new_wallet_amt}})
                    await ctx.send(f"Ohh you have bought Fidget Spinner! for {spinner_cost}!")
                elif spinner_cost == wallet:
                    new_wallet_amt = wallet-spinner_cost
                    author_inv_lap = inv_collection.update_one({"user": ctx.author.id}, {"$inc": {'fidget_spinner': amount}})
                    author_wallet_watch = collection.update_one({"user": ctx.author.id}, {"$set": {"wallet": new_wallet_amt}})
                    await ctx.send(f"Ohh you have bought Fidget Spinner! for {spinner_cost}!")
            elif item == "mobile_phone":
                mob_price = 7000
                mob_cost = mob_price*amount
                if wallet < mob_cost:
                    await ctx.send("You don't have enough money in your wallet!")
                elif mob_cost < wallet:
                    new_wallet_amt = wallet-mob_cost
                    author_inv_lap = inv_collection.update_one(
                        {"user": ctx.author.id}, {"$inc": {'mobile_phone': amount}})
                    author_wallet_watch = collection.update_one(
                        {"user": ctx.author.id}, {"$set": {"wallet": new_wallet_amt}})
                    await ctx.send(f"Ohh you have bought Mobile Phone! for {mob_cost}!")
                elif mob_cost == wallet:
                    new_wallet_amt = wallet-mob_cost
                    author_inv_lap = inv_collection.update_one(
                        {"user": ctx.author.id}, {"$inc": {'mobile_phone': amount}})
                    author_wallet_watch = collection.update_one(
                        {"user": ctx.author.id}, {"$set": {"wallet": new_wallet_amt}})
                    await ctx.send(f"Ohh you have bought Mobile Phone! for {mob_cost}!")
            elif item == 'bag_lock':
                bag_price = 13000
                bag_cost = bag_price*amount
                if wallet < bag_cost:
                    await ctx.send("You don't have enough money in your wallet!")
                elif bag_cost < wallet:
                    new_wallet_amt = wallet-bag_cost
                    author_inv_lap = inv_collection.update_one(
                        {"user": ctx.author.id}, {"$inc": {'bag_lock': amount}})
                    author_wallet_watch = collection.update_one(
                        {"user": ctx.author.id}, {"$set": {"wallet": new_wallet_amt}})
                    await ctx.send(f"Ohh you have bought Bag Lock! for {bag_cost}!")
                elif bag_cost == wallet:
                    new_wallet_amt = wallet-bag_cost
                    author_inv_lap = inv_collection.update_one(
                        {"user": ctx.author.id}, {"$inc": {'bag_lock': amount}})
                    author_wallet_watch = collection.update_one(
                        {"user": ctx.author.id}, {"$set": {"wallet": new_wallet_amt}})
                    await ctx.send(f"Ohh you have bought Bag Lock! for {bag_cost}!")
            elif item == 'hunting_rifle':
                rifle_price = 9000
                rifle_cost = rifle_price*amount
                if wallet < rifle_cost:
                    await ctx.send("You don't have enough money in your wallet!")
                elif rifle_cost < wallet:
                    new_wallet_amt = wallet-rifle_cost
                    author_inv_lap = inv_collection.update_one(
                        {"user": ctx.author.id}, {"$inc": {'hunting_rifle': amount}})
                    author_wallet_watch = collection.update_one(
                        {"user": ctx.author.id}, {"$set": {"wallet": new_wallet_amt}})
                    await ctx.send(f"Ohh you have bought Hunting Rifle! for {rifle_cost}!")
                elif rifle_cost == wallet:
                    new_wallet_amt = wallet-rifle_cost
                    author_inv_lap = inv_collection.update_one(
                        {"user": ctx.author.id}, {"$inc": {'hunting_rifle': amount}})
                    author_wallet_watch = collection.update_one(
                        {"user": ctx.author.id}, {"$set": {"wallet": new_wallet_amt}})
                    await ctx.send(f"Ohh you have bought Hunting Rifle! for {rifle_cost}!")
            elif item == 'apple':
                apple_price = 25
                apple_cost = apple_price*amount
                if wallet < apple_cost:
                    await ctx.send("You don't have enough money in your wallet!")
                elif apple_cost < wallet:
                    new_wallet_amt = wallet-apple_cost
                    author_inv_lap = inv_collection.update_one(
                        {"user": ctx.author.id}, {"$inc": {'apple': amount}})
                    author_wallet_watch = collection.update_one(
                        {"user": ctx.author.id}, {"$set": {"wallet": new_wallet_amt}})
                    await ctx.send(f"Ohh you have bought Apple! for {apple_cost}!")
                elif apple_cost == wallet:
                    new_wallet_amt = wallet-apple_cost
                    author_inv_lap = inv_collection.update_one(
                        {"user": ctx.author.id}, {"$inc": {'apple': amount}})
                    author_wallet_watch = collection.update_one(
                        {"user": ctx.author.id}, {"$set": {"wallet": new_wallet_amt}})
                    await ctx.send(f"Ohh you have bought Apple! for {apple_cost}!")
            elif item == 'cookie':
                cook_price = 15
                cook_cost = cook_price*amount
                if wallet < cook_cost:
                    await ctx.send("You don't have enough money in your wallet!")
                elif cook_cost < wallet:
                    new_wallet_amt = wallet-cook_cost
                    author_inv_lap = inv_collection.update_one(
                        {"user": ctx.author.id}, {"$inc": {'cookie': amount}})
                    author_wallet_watch = collection.update_one(
                        {"user": ctx.author.id}, {"$set": {"wallet": new_wallet_amt}})
                    await ctx.send(f"Ohh you have bought Cookie! for {cook_cost}!")
                elif cook_cost == wallet:
                    new_wallet_amt = wallet-cook_cost
            
                    author_inv_lap = inv_collection.update_one(
                        {"user": ctx.author.id}, {"$inc": {'cookie': amount}})
                    author_wallet_watch = collection.update_one(
                        {"user": ctx.author.id}, {"$set": {"wallet": new_wallet_amt}})
                    await ctx.send(f"Ohh you have bought Cookie! for {cook_cost}!")
            else:
                await ctx.send("**That Item Is Not Even there in the shop!**WHAT AN IDIOT!")
     
    @commands.command(help="Use the command for using things in your inventory such as an apple or a mobile phone if you have!?")
    async def use(self, ctx, thing=None):
        bankinfo = collection.find_one({"user":ctx.author.id})
        invinfo = inv_collection.find_one({"user":ctx.author.id})
        if not bankinfo:
            await ctx.send("You dont have an account creating one for you!...")
            collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0})
            inv_collection.insert_one({"user": ctx.author.id, "watch": 0, "second_hand_laptop": 0, "hunting_rifle": 0,"fidget_spinner": 0, "fishing_rod": 0, "mobile_phone": 0, "bag_lock": 0, "apple": 0, "cookie": 0})
            return
        else:
            if thing == None:
                await ctx.send("Bruh! What do you want to use!")
            elif thing == 'mobile_phone':
                mobile_check_user = invinfo["mobile_phone"]
                if mobile_check_user > 0:
                    await ctx.send(f"**{ctx.author.mention} What do you want to use the mobile phone for\n`p`-- Call The Police in case of robbery\n`s`--SMS your friend!\n`d`--Call The Devs\n`c`--Check If Someone Has added you as a friend!**")
                    def check(m):
                        return m.channel == ctx.channel
                    msg = await self.bot.wait_for('message', check=check, timeout=15.0)
                    if asyncio.TimeoutError:
                        await ctx.send("Ok looks like I should shut the Phone off!")
                    else:
                        if msg.content == 'p':
                            await ctx.send(f"`**With the police on a call!**`\n**{ctx.author.name}** Hello, Officer? There has been a robbery here!")
                            await asyncio.sleep(2)
                            await ctx.send(f"**Police Officer** What the hell are you talking bout I had that area checked no robbery took place **what an idiot** And please call us only if there is an actual emergency! Idiot!")
                            await asyncio.sleep(1)
                            await ctx.send("`Call disconnected!`")
                        elif msg.content == 's':
                            await ctx.reply("Whom do you want to send SMS to reply withing 10 seconds with a valid user!")
                            def user_check(m):
                                return m.channel == ctx.channel
                            msg1 = await self.bot.wait_for('message', check=user_check)
                            await ctx.send("`Message sent!`")
                        elif msg.content == 'd':
                            await ctx.send("`Calling the devs!`")
                            await ctx.send(f"**{ctx.author}** Is Blank-Chump mad?")
                            await ctx.send(f"**DEVS**, Not as mad as you!?")
                        elif msg.content == 'c':
                            await ctx.send("`Checking if someone has added you as a friend on discord...`")
                            await ctx.send("**Check Completed**, No one wants you as their friend lol!")
                else:
                    await ctx.reply("Hey you idiot you dont have a mobile phone to use it!")
            elif thing == 'apple':
                apple_check_user = invinfo["apple"]
                if apple_check_user > 0:
                    mon = random.randrange(50, 100)
                    await ctx.send(f"You ate an apple and your energy increased! you also got {mon}")
                    collection.update_one({"user":ctx.author.id}, {"$inc":{"wallet":mon}})
                    inv_collection.update_one({"user":ctx.author.id}, {"$set":{"apple":apple_check_user-1}})
                else:
                    await ctx.send("You dont have an apple to use it!")
    
    @commands.command()
    @commands.is_owner()
    async def sell(self, ctx, item, amount=1):
        bankinfo = collection.find_one({"user":ctx.author.id})
        if not bankinfo:
            await ctx.send("You dont have an account creating one for you!...")
            collection.insert_one({"user": ctx.author.id, "wallet": 0, "bank": 0})
            inv_collection.insert_one({"user": ctx.author.id, "watch": 0, "second_hand_laptop": 0, "hunting_rifle": 0, "fidget_spinner": 0, "fishing_rod": 0, "mobile_phone": 0, "bag_lock": 0, "apple": 0, "cookie": 0})
            return
        else:
            inventory = inv_collection.find_one({"user":ctx.author.id})
            for item in inventory:
                if inventory[item] > 0:
                    return

    @commands.command()
    async def search(self, ctx):
        l1 = random.choice(['discord', 'world wide web', 'cupboard', 'desk'])
        l2 = random.choice(['your pant', 'your bag', 'coffin', 'coat'])
        l3 = random.choice(['washroom', 'attic', 'neighbours house'])
        await ctx.send(f'Hey {ctx.author.mention} **Where do you want to search?**\n*Pick from the options below and send in the chat*\n`{l1}`, `{l2}`, `{l3}`')
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        msg = await self.bot.wait_for('message', check=check)
        if msg.content == l1 or l2 or l3:
            earning = random.randrange(300, 1500)
            await ctx.send(f"You searched {msg.content} and earned {earning} coins!")
            collection.update_one({"user":ctx.author.id}, {"$inc":{"wallet":earning}})
        else:
            await ctx.send(f"Hey {ctx.author.mention} thats not a valid option!")




def setup(bot):
    bot.add_cog(Currency(bot))
