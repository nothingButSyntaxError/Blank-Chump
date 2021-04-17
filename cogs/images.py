import discord
from discord import user
from discord import file
from discord.ext import commands, tasks
import random
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from io import BytesIO
import textwrap

from discord.team import TeamMember


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

    @commands.command()
    async def captain_marvel(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        cap = Image.open("./cogs/img_src/captain_marvel.jpg")
        asset = member.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((138, 166))
        cap.paste(pfp, (320, 129))
        cap.save("captain_marvel_pfp.jpg")
        await ctx.send(file=discord.File("captain_marvel_pfp.jpg"))
    
    @commands.command()
    async def uglier(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        ugly = Image.open("./cogs/img_src/ugly.png")
        asset = member.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((176, 172))
        ugly.paste(pfp, (120, 56))
        ugly.save("ugly_pfp.png")
        await ctx.send(file=discord.File("ugly_pfp.png"))

    @commands.command()
    async def dog(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        dog = Image.open("./cogs/img_src/dog.jfif")
        asset = member.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((142, 170))
        dog.paste(pfp, (277, 62))
        dog.save("dog_pfp.png")
        await ctx.send(file=discord.File("dog_pfp.png"))

    @commands.command()
    async def whiteboard(self, ctx, *, text):
        if len(text) > 30:
            await ctx.send("The words should be less than 10")
        elif len(text) < 30:
            wrapper = textwrap.TextWrapper(width=22)
            word_list = wrapper.wrap(text=str(text))
            board = Image.open("./cogs/img_src/blankboard.jpg")
            draw = ImageDraw.Draw(board)
            font = ImageFont.truetype("believe_font.ttf", 30)
            draw.text((159, 118), word_list, (0,0,0), font=font)
            board.save("board_pfp.jpg")
            await ctx.send(file=discord.File("board_pfp.jpg"))

    @commands.command()
    async def cat(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        cat = Image.open("./cogs/img_src/cat.jpg")
        asset = member.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((889, 807))
        cat.paste(pfp, (219, 649))
        cat.save("cat_pfp.png")
        await ctx.send(file=discord.File("cat_pfp.png"))


    @commands.command(aliases=['trash'])
    async def garbage(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        garbage = Image.open("./cogs/img_src/garbage.jpg")
        asset = member.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((255, 246))
        og_pfp = pfp.filter(ImageFilter.GaussianBlur(4))
        garbage.paste(og_pfp, (216, 0))
        garbage.save("garbage_pfp.jpg")
        await ctx.send(file=discord.File("garbage_pfp.jpg"))

    @commands.command()
    async def mandalorian(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        mando = Image.open("./cogs/img_src/mando.jpeg")
        asset = member.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((324, 349))
        mando.paste(pfp, (507, 21))
        mando.save("mando_pfp.jpeg")
        await ctx.send(file=discord.File("mando_pfp.jpeg"))

   
    

def setup(bot):
    bot.add_cog(Images(bot))
