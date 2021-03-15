import asyncio
import discord
from discord.ext import commands
import os
import random


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


#search google command sends link for lmgtfy
    @commands.command(help = "Searches whatever you want on google", aliases = ["Search"])
    @commands.guild_only()
    async def google(self, ctx, term):
        link = f"http://lmgtfy.com/?q={term}"
        embed = discord.Embed(title="LMGTFY", url=f"https://lmgtfy.com/?q={term}", description="Cant do anything more than this find your query by going on this link lazy idiot!")
        await ctx.send(link, embed=embed)


    @google.error
    async def google_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You have to send what you want to google with the command!")

     
    @commands.command(help = "Types your word again with claps")
    @commands.guild_only()
    async def clap(self,ctx,term):
        letters = len(term)
        if letters:
            for letter in term:
                await ctx.send(f"{letter}:clap:" )
        else:
            await ctx.send("Type something to clap you dumbo:laughing:")   
                    

    @commands.command(help = "Doots all your words")
    @commands.guild_only()
    async def doot(self,ctx,term):
        letters = len(term)
        if letters:
            for letter in term:
                await ctx.send(f"{letter}💀🎺" )
        else:
            await ctx.send("Type something to doot you dumbo:laughing:")   


    @commands.command(help = "Roasts the person you mention", aliases = ["insult"])
    @commands.guild_only()
    async def roast(self, ctx, member: discord.Member = None):
        roast = random.choice(["You are a pizza burn on the roof of the world's mouth","You losing your virginity is like a summer squash growing in the middle of winter. Never happening","You are dumber than a block of wood and not nearly as useful","You’re the reason God created the middle finger.","You’re a grey sprinkle on a rainbow cupcake.","If your brain was dynamite, there wouldn’t be enough to blow your hat off"," You are more disappointing than an unsalted pretzel.","Light travels faster than sound which is why you seemed bright until you spoke."," You have so many gaps in your teeth it looks like your tongue is in jail.","Your face makes onions cry.","Don’t be ashamed of who you are. That’s your parents’ job."])
        if member == None:
            await ctx.send(f"{roast}") 
        elif member != None:
            await ctx.send(f"{member.mention} {roast}") 


    @commands.command(help = "Answers all your questions with either a yes or a no")
    @commands.guild_only()
    async def _8ball(self, ctx, *, question):
        _8ball = random.choice(["Yes, you noob ","No, I guess"])
        if question :
            await ctx.send(f":8ball: {_8ball}") 
        else:
            await ctx.send("Please state your question") 


    @commands.command(help = "Repeats everything that you say", aliases = ["print"])
    @commands.guild_only()
    async def  say(self, ctx, *, sentence):
        if sentence :
            await ctx.send(f"{sentence} \n\n -{ctx.author}")
        else:
            await ctx.send("Please type a sentence to be said")


    @commands.command(help = "Rates how simp you are", aliases=["simpr8"])
    @commands.guild_only()
    async def simprate(self, ctx, member: discord.Member = None):
        simp = random.randrange(1,100)
        if member :
            embed = discord.Embed(title = f"Simp Rate machine \n\n {member} is {simp}% simp", colour = discord.Colour.dark_red())
            await ctx.send(embed = embed)
        else:
            embed_1 = discord.Embed(title = f"Simp Rate machine \n\n {ctx.author.name} is {simp}% simp", colour = discord.Colour.dark_red())
            await ctx.send(embed = embed_1)


    @commands.command(help = "Rates how dank you are", aliases=["dankr8"])
    @commands.guild_only()
    async def dankrate(self, ctx, member: discord.Member = None):
        dank = random.randrange(1,100)
        if member:
           embed = discord.Embed(title = f"Dank Rate machine \n\n {member} is {dank}% dank", colour = discord.Colour.gold())
           await ctx.send(embed = embed)
        else:
            embed_1 = discord.Embed(title = f"Dank Rate machine \n\n {ctx.author.name} is {dank}% dank", colour = discord.Colour.gold())
            await ctx.send(embed = embed_1)


    @commands.command(help = "Rates how stank you are", aliases=["stankr8"])
    @commands.guild_only()
    async def stankrate(self, ctx, member: discord.Member = None):
        stank = random.randrange(1,100)
        if member == None:
            embed = discord.Embed(title = f"Stank Rate machine \n\n {member} is {stank}% stank", colour = discord.Colour.teal())
            await ctx.send(embed = embed)
        else:
            embed_1 = discord.Embed(title = f"Stank Rate machine \n\n {ctx.author.name} is {stank}% stank", colour = discord.Colour.teal())
            await ctx.send(embed = embed_1)


    @commands.command(help = "Rates how cool you are", aliases=["coolr8"])
    @commands.guild_only()
    async def coolrate(self, ctx, member: discord.Member = None):
        cool = random.randrange(1,100)
        if member :
            embed = discord.Embed(title = f"Cool Rate machine \n\n {member} is {cool}% cool", colour = discord.Colour.blue())
            await ctx.send(embed = embed)
        else:
            embed_1 = discord.Embed(title = f"Cool Rate machine \n\n {ctx.author.name} is {cool}% cool", colour = discord.Colour.blue())
            await ctx.send(embed = embed_1)


    @commands.command(help = "Rates how chump you are", aliases=["chumpr8"])
    @commands.guild_only()
    async def chumprate(self, ctx, member: discord.Member = None):
        chump = random.randrange(1,100)
        if member :
            embed = discord.Embed(title = f"Chump Rate machine \n\n {member} is {chump}% chump", colour = discord.Colour.green())
            await ctx.send(embed = embed)
        else:
            embed_1 = discord.Embed(title = f"Chump Rate machine \n\n {ctx.author.name} is {chump}% chump", colour = discord.Colour.green())
            await ctx.send(embed = embed_1)


    @commands.command(help = "Rates how epic you are as a gamer", aliases=["egr8"])
    @commands.guild_only()
    async def epicgamerrate(self, ctx, member: discord.Member = None):
        epicgamer = random.randrange(1,100)
        if member :
            embed = discord.Embed(title = f"Epic Gamer Rate machine :video_game: \n\n {member} is {epicgamer}% epic gamer", colour = discord.Colour.gold())
            await ctx.send(embed = embed)
        else:
            embed_1 = discord.Embed(title = f"Epic Gamer Rate machine :video_game: \n\n {ctx.author.name} is {epicgamer}% epic gamer", colour = discord.Colour.gold())
            await ctx.send(embed = embed_1)


    @commands.command(help = "Rates how waifu you are", aliases=["waifur8"])
    @commands.guild_only()
    async def waifurate(self, ctx, member: discord.Member = None):
       waifu = random.randrange(1,100)
       if member :
            embed = discord.Embed(title = f"Waifu Rate machine \n\n {member} is {waifu}% waifu", colour = discord.Colour.dark_magenta())
            await ctx.send(embed = embed)
       else:
            embed_1 = discord.Embed(title = f"Waifu Rate machine \n\n {ctx.author.name} is {waifu}% waifu", colour = discord.Colour.dark_magenta())
            await ctx.send(embed = embed_1)


    @commands.command(help = "Rates how gay you are", aliases=["gayr8", "gayrate"])
    @commands.guild_only()
    async def howgay(self, ctx, member: discord.Member = None):
        gay = random.randrange(1,100)
        if member :
            embed = discord.Embed(title = f"Gay Rate machine \n\n {member} is {gay}% gay", colour = discord.Colour.purple())
            await ctx.send(embed = embed)
        else:
            embed_1 = discord.Embed(title = f"Gay Rate machine \n\n {ctx.author.name} is {gay}% gay", colour = discord.Colour.purple())
            await ctx.send(embed = embed_1)
    

    @commands.command(help = "Ranks how thoughtful you are", aliases = ["thotr8", "thotrate",])
    @commands.guild_only()
    async def rankthot(self, ctx, member: discord.Member = None ):
        thot = random.randrange(1,100)
        if member :
            embed = discord.Embed(title = f"Thought Rate machine \n\n {member} is {thot}% thoughtful", colour = discord.Colour.purple())
            await ctx.send(embed = embed)
        else:
            embed_1 = discord.Embed(title = f"Thought Rate machine \n\n {ctx.author.name} is {thot}% thoughtful", colour = discord.Colour.purple())
            await ctx.send(embed = embed_1)


    @commands.command(help = "Hacks the person who you mention", aliases = ["datarob"])
    @commands.guild_only()
    async def hack(self, ctx, member: discord.Member = None):
        if member == None:
            await ctx.send("You need to name someone to hack!!!")
        else: 
            msg = await ctx.send(f"Hacking {member.name} now")
            await asyncio.sleep(2)
            await msg.edit(content = "Adding all information to database" )
            await asyncio.sleep(2)
            await msg.edit(content = "Sending data to government")
            await asyncio.sleep(2)
            await msg.edit(content = "Sending all data secrets to you")
            await asyncio.sleep(2)
            await msg.edit(content = "Loading virus in the software...")
            await asyncio.sleep(2)
            await msg.edit(content = "Spreading data around the internet to see")
            await asyncio.sleep(2)
            await msg.edit(content = "The totally real and actually existing hack is complete.")
    

    @commands.command(help = "Redacts any message you send", aliases = ["redactor"] )
    @commands.guild_only()
    async def spoiler(self, ctx, *, redacteds = None):
        if redacteds == None :
             await ctx.send("You need to send some words to be redacted")
        else :
            for redacted in redacteds :
                blackwords= (f"||{redacted}||")
            await ctx.send(blackwords)

    
    @commands.command(help = "It says OwO", aliases = ["OwO"])
    @commands.guild_only()
    async def owo(self, ctx):
        await ctx.send("OwO")

    @commands.command(help = "Vaporwaves your words. Try it out")
    @commands.guild_only()
    async def vaporwave(self,ctx, *, term = None):
        if term!= None:
            for letter in term:
                await ctx.send(f"{letter} " )
        elif term == None:
            await ctx.send("Type something to vaporwave you dumbo:laughing:")  


    @commands.command(help = "Rickrolls any member of discord on your behalf.", aliases = ["astley", "prank"])  
    async def rickroll(self, ctx, member: discord.Member = None):
        if member != None:
            msg = await member.send(f"{ctx.author.name} has sent this special link for you \n https://youtu.be/dQw4w9WgXcQ")
            await msg.edit(suppress = True )
            await ctx.message.delete() 
        else:
            await ctx.send("You have to mention a member to rickroll, or I will rickroll you :smiley: ")
    

#Converts to emojis
    @commands.command(help = "Converts your output into emojis you can send to your friends", aliases = ["emojiconvert", "textconvert"])
    @commands.guild_only()
    async def emojify(self, ctx, *, term):
        emojis = {"a":":regional_indicator_a:", 'b':':regional_indicator_b:',"c":":regional_indicator_c:","d":":regional_indicator_d:",'e':':regional_indicator_e:','f':':regional_indicator_f:','g':':regional_indicator_g:','h':':regional_indicator_h:','i':':regional_indicator_i:','j':':regional_indicator_j:','k':':regional_indicator_k:','l':':regional_indicator_l:','m':':regional_indicator_m:','n':':regional_indicator_n:','o':':regional_indicator_o:','p':':regional_indicator_q:','r':':regional_indicator_r:','s':':regional_indicator_s:','t':':regional_indicator_t:','u':':regional_indicator_v:','w':':regional_indicator_w:','x':':regional_indicator_x:','y':':regional_indicator_y:','z':':regional_indicator_z:', '1':':one:', '2':':two:','3':':three:','4':':four:','5':':five:','6':':six:','7':':seven:','8':':eight:','9':':nine:','0':':zero:',"`":"`","~":"~","!":":grey_exclamation:","@":"@",'#':":hash:","$":"$","%":"%","^":"^","&":"&","*":":asterisk:","(":"(",")":")","_":"_","-":"-","+":"+","=":"=","{":"{","}":"}","[":"[","]":"]",'|':"|",":":":",";":";",'"':'"',"'":"'","<":"<",",":",",">":">",".":".","?":":grey_question:","/":"/"}        
        for letter in term.lower():
            term_emojis = emojis[letter]
            await ctx.send(term_emojis)
    
#compliments similar code to roasts
    @commands.command(help = "Compliment the person you mention", aliases = ["comp","appreciate"])
    @commands.guild_only()
    async def compliment(self, ctx, member: discord.Member = None):
        comp = random.choice(["Your smile is contagious.",
        "I bet you make babies smile.", 
        "You have the best laugh.",
        "You light up the room.",
        "You have a great sense of humor.",
        "If cartoon bluebirds were real, a couple of 'em would be sitting on your shoulders singing right now.",
        "You're like sunshine on a rainy day.",
        "You bring out the best in other people.",
        "I bet you sweat glitter.",
        "Colors seem brighter when you're around.",
        "You're more fun than a ball pit filled with candy.",
        "Jokes are funnier when you tell them.",
        "You always know how to find that silver lining.",
        "You're a candle in the darkness.",
        "Being around you is like a happy little vacation.",
        "You're more fun than bubble wrap.",
        "You're like a breath of fresh air.",
        "You're someone's reason to smile.",
        "How do you keep being so funny and making everyone laugh?",
        "You have impeccable manners.",
        "I like your style.",
        "You're strong.",
        'Is that your picture next to "charming" in the dictionary?',
        'Your kindness is a balm to all who encounter it.',
        'You are brave.',
        'Your insides are even more beautiful than your outside.',
        'You have the courage of your convictions.',
        "You're a great listener.",
        'You were cool way before hipsters were cool.',
        "That thing you don't like about yourself is what makes you really interesting.",
        "You're inspiring.",
        "You're so thoughtful.",
        "When you make up your mind, nothing stands in your way.",
        'You seem to really know who you are.',
        "You're a smart cookie.",
        'Your perspective is refreshing.',
        'Your ability to recall random factoids at just the right times is impressive.',
        'When you say, "I meant to do that," I totally believe you.',
        'You have the best ideas.',
        "You're always learning new things and trying to better yourself. That's awesome.",
        'If someone based an Internet meme on you, it would have impeccable grammar.',
        'You could survive a zombie apocalypse.',
        'When you make a mistake, you fix it.',
        "You're great at figuring stuff out.",
        'Your creative potential seems limitless.',
        'I bet you do crossword puzzles in ink.',
        'You have a good head on your shoulders.',
        'Everyone gets knocked down sometimes; only people like you get back up again and keep going.',
        'You should be proud of yourself.',
        'You are making a difference.',
        'You deserve a hug right now.',
        "You're a great example to others.",
        'Actions speak louder than words, and yours tell an incredible story.',
        "You're an awesome friend.",
        "You're more helpful than you realize.",
        'Hanging out with you is always fun.',
        "That thing where you know when someone needs something? That's amazing.",
        'Being around you makes everything better.',
        'You should be thanked more often. Thank you.',
        "Our community is better because you're in it."
        "Someone is getting through something hard right now because you've got their back. Nice work.",
        'You always know just what to say.',
        'The people you love are lucky to have you in their lives.',
        'Any team would be lucky to have you on it.',
        'Defenseless animals are drawn to you.',
        'The way you treasure your loved ones is incredible.',
        "You're a gift to those around you.",
        'I appreciate you.',
        'You are the most perfect you there is.',
        'You are enough.',
        "You're all that and a super-size bag of chips.",
        "On a scale from 1 to 10, you're an 11.",
        "You've got all the right moves.",
        'Everything would be better if more people were like you.',
        "When you're not afraid to be yourself, that's when you're incredible.",
        "You're wonderful.",
        "You're better than a triple-scoop ice cream cone. With sprinkles.",
        "You're one of a kind.",
        "If you were a box of crayons, you'd be the big industrial name-brand one with a built-in sharpener.",
        "Who raised you? They deserve a medal for a job well done.",
        "Somehow you make time stop and fly all at the same time.",
        'In high school, I bet you were voted "most likely to continue being awesome."',
        "If you were a scented candle they'd have to call it Perfectly Imperfect (and it would smell like summer).",
        "There's ordinary, and then there's you.",
        "You're even better than a unicorn because you're real.",
        "You're really something special."])
        if member == None:
            await ctx.send(f"{ctx.author.name} {comp}") 
        elif member != None:
            await ctx.send(f"{member.mention} {comp}")
    









    




    
    

    


    

    

           

    


def setup(bot):
    bot.add_cog(Fun(bot))
    