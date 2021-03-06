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
            embed = discord.Embed(title=f"{member.name}'s balance", description=f"\n\n**WALLET:** {wallet}\n**BANK:** {bank}\n**NET WORTH:** {net_worth}", colour=discord.Colour.blue())
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
    @commands.check(pm_check)
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

    @postmeme.error
    async def postmeme_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You need to buy a laptop for posting memes on the internet! Buy it using `%buy second_hand_laptop`")

    
    @commands.command()
    @commands.check(fish_check)
    async def fish(self, ctx):
        fish_type = random.choice(['common fish', 'rare fish', 'epic fish', 'legendary fish', 'common fish', 'common fish', 'common fish', 'rare fish', 'rare fish', 'epic fish', 'legendary fish'])
        amount_fish = random.randrange(1, 5)
        await ctx.send("This command is under development! Please dont use!?")


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




def setup(bot):
    bot.add_cog(Currency(bot))
