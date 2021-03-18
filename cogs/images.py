import discord
from discord.ext import commands
import random
from PIL import Image
from io import BytesIO


class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wanted(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        wanted = Image.open("./cogs/img_src/wanted.jpeg")
        asset = member.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((381, 294))
        wanted.paste(pfp, (45, 225))
        wanted.save("wanted_pfp.jpeg")
        await ctx.send(file=discord.File("wanted_pfp.jpeg"))

    @commands.command()
    async def rip(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        rip = Image.open("./cogs/img_src/rip.png")
        asset = member.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((162, 168))
        rip.paste(pfp, (111, 244))
        rip.save("rip_pfp.png")
        await ctx.send(file=discord.File("rip_pfp.png"))

    @commands.command()
    async def thanos(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        thanos = Image.open("./cogs/img_src/thanos.jpg")
        asset = member.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((215, 275))
        thanos.paste(pfp, (347, 81))
        thanos.save("thanos_pfp.jpg")
        await ctx.send(file=discord.File("thanos_pfp.jpg"))

    @commands.command()
    async def thanos(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        thanos = Image.open("./cogs/img_src/thanos.jpg")
        asset = member.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((215, 275))
        thanos.paste(pfp, (347, 81))
        thanos.save("thanos_pfp.jpg")
        await ctx.send(file=discord.File("thanos_pfp.jpg"))

    @commands.command(aliases=['wdt'])
    async def whodidthis(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        wdt = Image.open("./cogs/img_src/wdt.jfif")
        asset = member.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((250, 209))
        wdt.paste(pfp, (46, 74))
        wdt.save("wdt_pfp.jpg")
        await ctx.send(file=discord.File("wdt_pfp.jpg"))

    @commands.command()
    async def ipad(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        ipad = Image.open("./cogs/img_src/ipad.jpg")
        asset = member.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((394, 528))
        ipad.paste(pfp, (363, 113))
        ipad.save("ipad_pfp.jpg")
        await ctx.send(file=discord.File("ipad_pfp.jpg"))

    


def setup(bot):
    bot.add_cog(Images(bot))
