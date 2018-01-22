import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = ".#")

@bot.command()
async def Owen():
    await bot.say("""
    Meet Creator #Owen!\n\n#Owen likes:%40s
        %s%45s
        %s%45s
        %s%45s
        %s
        %s
        
        """ % ("#Owen dislikes:", "like", "dislike", "like", "dislike", "like", "dislike", "like", "like"))

@bot.command()
async def Vignesh():
    await bot.say("""
    Meet Creator #Vignesh!\n\n#Vignesh likes:%40s
        %s%45s
        %s%45s
        %s%45s
        %s
        %s
        
        """ % ("#Vignesh dislikes:", "like", "dislike", "like", "dislike", "like", "dislike", "like", "like"))

@bot.command()
async def Amani():
    await bot.say("""
    Meet Creator #Amani!\n\n#Amani likes:%40s
        %s%45s
        %s%45s
        %s%45s
        %s
        %s
        
        """ % ("#Amani dislikes:", "like", "dislike", "like", "dislike", "like", "dislike", "like", "like"))


@bot.command()
async def AJ():
    await bot.say("""
    Meet Creator #A.J.!\n\n#A.J. likes:%40s
        %s%45s
        %s%45s
        %s%45s
        %s
        %s
        %s
        %s
        %s
        %s
        
        """ % ("#A.J. dislikes:", "Food", "Biology", "Hugs", "Homework", "Bananya", "Scary Movies", "Hedgehogs", "Otters", "Sherlock", "Macarons", "Harry Potter", "Mr. Respass"))
        



bot.run("NDAwNzA3NTQxODQ5NjA0MDk2.DTfj9w.fJ9ztMwA7NTFuiiyJXv0Tdvwzn4")
